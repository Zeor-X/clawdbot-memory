#!/usr/bin/env python3
"""
行情数据获取脚本 (真实数据源)
使用 Alpha Vantage API 获取美股
"""
import json
import sys
import os
import time
import requests
from datetime import datetime

SINA_API_BASE = 'https://hq.sinajs.cn'
ALPHA_VANTAGE_API_KEY = "3TZZQMPBYO4099V7"
ALPHA_VANTAGE_BASE_URL = "https://www.alphavantage.co/query"

# 尝试从环境变量读取 API Key
if os.getenv('ALPHA_VANTAGE_API_KEY'):
    ALPHA_VANTAGE_API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')

# 美股代码中文名称映射
US_STOCK_NAMES = {
    'AAPL': '苹果',
    'GOOGL': '谷歌',
    'MSFT': '微软',
    'NVDA': '英伟达',
    'TSLA': '特斯拉',
    'META': 'Meta',
    'AMZN': '亚马逊',
    'SPY': '标普500',
    'DIA': '道琼斯',
    'QQQ': '纳斯达克',
}

def get_stock_data_sina(stock_code):
    """从新浪财经获取 A 股数据"""
    try:
        if stock_code.endswith('.SH'):
            prefix = 'sh'
            code = stock_code.replace('.SH', '')
        elif stock_code.endswith('.SZ'):
            prefix = 'sz'
            code = stock_code.replace('.SZ', '')
        elif stock_code.startswith('6'):
            prefix = 'sh'
            code = stock_code
        else:
            prefix = 'sz'
            code = stock_code

        url = f"{SINA_API_BASE}/list={prefix}{code}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Referer': 'https://finance.sina.com.cn/',
        }

        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            content = response.text
            if '=' in content:
                data_str = content.split('=')[1].replace('"', '').replace(';', '')
                data_arr = data_str.split(',')

                if len(data_arr) > 6 and data_arr[0]:
                    name = data_arr[0]
                    price = float(data_arr[3]) if data_arr[3] else 0
                    open_price = float(data_arr[1]) if data_arr[1] else 0
                    pre_close = float(data_arr[2]) if data_arr[2] else 0
                    high = float(data_arr[4]) if len(data_arr) > 4 and data_arr[4] else 0
                    low = float(data_arr[5]) if len(data_arr) > 5 and data_arr[5] else 0

                    change = round(price - pre_close, 2)
                    percent = round((price - pre_close) / pre_close * 100, 2) if pre_close > 0 else 0

                    print(f"✅ {name}({prefix}{code}): ¥{price} {change:+.2f} ({percent:+.2f}%)")
                    return {
                        'name': name,
                        'code': code,
                        'prefix': prefix,
                        'price': price,
                        'open': open_price,
                        'pre_close': pre_close,
                        'high': high,
                        'low': low,
                        'change': change,
                        'percent': percent,
                        'currency': '¥'
                    }
    except Exception as e:
        print(f"⚠️ {stock_code} 获取失败: {str(e)[:50]}")
    return None

def get_us_stock_alphavantage(symbol):
    """
    从 Alpha Vantage 获取美股数据
    需要 API Key: https://www.alphavantage.co/support/#api-key
    """
    if ALPHA_VANTAGE_API_KEY == "ALPHA_VANTAGE_API_KEY_PLACEHOLDER":
        print("⚠️ Alpha Vantage API Key 未设置，跳过美股数据获取")
        return None

    try:
        params = {
            "function": "GLOBAL_QUOTE",
            "symbol": symbol,
            "apikey": ALPHA_VANTAGE_API_KEY
        }

        response = requests.get(ALPHA_VANTAGE_BASE_URL, params=params, timeout=15)
        data = response.json()

        if "Global Quote" not in data:
            print(f"⚠️ {symbol} 返回数据无效: {data.get('Note', data)}")
            return None

        quote = data["Global Quote"]
        
        if not quote:
            print(f"⚠️ {symbol} 无数据")
            return None

        # Alpha Vantage 返回的字段名
        price = float(quote.get('05. price', 0))
        change = float(quote.get('09. change', 0))
        change_percent_str = quote.get('10. change percent', '0%').replace('%', '').strip()
        percent = float(change_percent_str)
        open_price = float(quote.get('02. open', 0))
        high = float(quote.get('03. high', 0))
        low = float(quote.get('04. low', 0))
        
        # 使用中文名称映射（如果有），否则使用 symbol
        symbol_upper = symbol.upper()
        name = US_STOCK_NAMES.get(symbol_upper, symbol_upper)

        print(f"✅ {name}: ${price:.2f} {change:+.2f} ({percent:+.2f}%)")
        return {
            'name': name,
            'code': symbol.upper(),
            'price': price,
            'change': change,
            'percent': percent,
            'open': open_price,
            'high': high,
            'low': low,
            'currency': '$'
        }

    except Exception as e:
        print(f"⚠️ {symbol} Alpha Vantage 获取失败: {str(e)[:50]}")
        return None

def get_multiple_stocks(stock_codes, is_us_stock=False):
    """获取多只股票数据"""
    results = {}
    for code in stock_codes:
        if is_us_stock:
            data = get_us_stock_alphavantage(code)
            if data:
                results[data['code']] = data
            time.sleep(12)  # Alpha Vantage 免费版限制: 5 calls/minute
        else:
            data = get_stock_data_sina(code)
            if data:
                results[data['code']] = data
            time.sleep(0.5)  # 避免请求过快
    return results

def format_stock_report(stocks_data, indices_data=None, us_indices_data=None, us_stocks_data=None):
    """格式化行情报告"""
    report = f"""
📊 **行情报告 (真实数据)**
⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
━━━━━━━━━━━━━━━━━━
"""

    # A股大盘指数
    if indices_data:
        report += "🎯 **A股大盘指数**\n"
        for code in ['000001', '399001', '399006']:
            if code in indices_data:
                idx = indices_data[code]
                symbol = '📈' if idx['percent'] > 0 else '📉'
                symbol = '➡️' if idx['percent'] == 0 else symbol
                report += f"• {idx['name']} {symbol} {idx['price']:.2f} ({idx['percent']:+.2f}%)\n"
        report += "\n"

    # A股个股关注
    report += "💰 **A股个股关注**\n"
    if stocks_data:
        for code, stock in stocks_data.items():
            symbol = '📈' if stock['percent'] > 0 else '📉'
            symbol = '➡️' if stock['percent'] == 0 else symbol
            report += f"• {stock['name']}({stock['prefix']}{stock['code']}) {symbol} ¥{stock['price']:.2f} ({stock['percent']:+.2f}%)\n"
    else:
        report += "⚠️ 暂无A股个股数据\n"

    report += "\n"

    # 美股大盘指数
    report += "🇺🇸 **美股大盘指数**\n"
    if us_indices_data:
        for code, stock in us_indices_data.items():
            symbol = '📈' if stock['percent'] > 0 else '📉'
            symbol = '➡️' if stock['percent'] == 0 else symbol
            report += f"• {stock['name']} {symbol} ${stock['price']:.2f} ({stock['percent']:+.2f}%)\n"
    else:
        if ALPHA_VANTAGE_API_KEY == "ALPHA_VANTAGE_API_KEY_PLACEHOLDER":
            report += "⚠️ API Key 未配置\n"
        else:
            report += "⚠️ 暂无美股指数数据\n"
    report += "\n"

    # 美股个股关注
    if us_stocks_data:
        report += "💰 **美股个股关注**\n"
        for code, stock in us_stocks_data.items():
            symbol = '📈' if stock['percent'] > 0 else '📉'
            symbol = '➡️' if stock['percent'] == 0 else symbol
            # 显示 中文名称(代码) 格式
            display_name = stock['name'] if stock['name'] != stock['code'] else stock['code']
            report += f"• {display_name}({stock['code']}) {symbol} ${stock['price']:.2f} ({stock['percent']:+.2f}%)\n"
    else:
        report += "💰 **美股个股关注**\n"
        if ALPHA_VANTAGE_API_KEY == "ALPHA_VANTAGE_API_KEY_PLACEHOLDER":
            report += "⚠️ API Key 未配置 (设置环境变量 ALPHA_VANTAGE_API_KEY)\n"
        else:
            report += "⚠️ 暂无美股数据\n"

    report += "\n---\n*数据来源: 新浪财经(A股) + Alpha Vantage(美股)*"
    return report

def main():
    print("🚀 行情数据获取脚本启动 (真实数据源)")
    print(f"⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    if ALPHA_VANTAGE_API_KEY == "ALPHA_VANTAGE_API_KEY_PLACEHOLDER":
        print("⚠️ Alpha Vantage API Key 未设置")
        print("   获取免费 API Key: https://www.alphavantage.co/support/#api-key")
        print("   然后设置环境变量: export ALPHA_VANTAGE_API_KEY=你的key")
    
    print("-" * 50)

    # 获取A股指数
    print("📡 获取A股指数数据...")
    index_codes = ['000001.SH', '399001.SZ', '399006.SZ']
    indices_data = get_multiple_stocks(index_codes)

    # 获取A股个股
    print("\n📡 获取A股个股数据...")
    stock_codes = ['600519.SH', '300750.SZ', '002594.SZ', '601318.SH', '000858.SZ']
    stocks_data = get_multiple_stocks(stock_codes)

    # 获取美股指数（如果有API Key）
    us_indices_data = {}
    if ALPHA_VANTAGE_API_KEY != "ALPHA_VANTAGE_API_KEY_PLACEHOLDER":
        print("\n📡 获取美股指数...")
        us_index_codes = ['SPY', 'DIA', 'QQQ']  # S&P 500, 道琼斯, 纳斯达克 ETF
        us_indices_data = get_multiple_stocks(us_index_codes, is_us_stock=True)

    # 获取美股
    us_stocks_data = {}
    if ALPHA_VANTAGE_API_KEY != "ALPHA_VANTAGE_API_KEY_PLACEHOLDER":
        print("\n📡 获取美股数据...")
        us_stock_codes = ['AAPL', 'GOOGL', 'MSFT', 'NVDA', 'TSLA']
        us_stocks_data = get_multiple_stocks(us_stock_codes, is_us_stock=True)

    if not stocks_data and not indices_data and not us_stocks_data:
        print("\n❌ 无法获取任何数据")
        return 1

    print("\n" + "=" * 50)
    print("✅ 数据获取完成")

    # 格式化报告
    report = format_stock_report(stocks_data, indices_data, us_indices_data, us_stocks_data)
    print(report)

    # 保存报告
    os.makedirs('/root/clawd/reports', exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')

    with open(f'/root/clawd/reports/stock-report-{timestamp}.md', 'w', encoding='utf-8') as f:
        f.write(report)

    with open('/root/clawd/reports/stock-latest.md', 'w', encoding='utf-8') as f:
        f.write(report)

    with open('/root/clawd/reports/stock-latest.json', 'w', encoding='utf-8') as f:
        json.dump({
            'timestamp': datetime.now().isoformat(),
            'success': True,
            'indices_count': len(indices_data),
            'stocks_count': len(stocks_data),
            'us_stocks_count': len(us_stocks_data)
        }, f, ensure_ascii=False, indent=2)

    print(f"\n✅ 报告已保存")

    with open('/root/clawd/reports/stock-send-request.txt', 'w') as f:
        f.write(datetime.now().isoformat())
    print("✅ 发送请求已记录")

    return 0

if __name__ == '__main__':
    sys.exit(main())
