# 每日资讯总结 - 定时任务配置

## 📊 已创建的脚本

### 1. daily-summary-report.sh
- 生成包含 AI 资讯、市场行情、加密货币的综合报告
- 包含所有重要链接
- 位置: `/root/clawd/scripts/daily-summary-report.sh`

### 2. morning-daily-summary.sh
- 早间日报执行脚本
- 位置: `/root/clawd/scripts/morning-daily-summary.sh`

### 3. evening-daily-summary.sh
- 晚间日报执行脚本
- 位置: `/root/clawd/scripts/evening-daily-summary.sh`

## ⏰ 配置定时任务

需要使用 Clawdbot cron 添加两个定时任务：

### 早间日报（早上 8:00）
```bash
clawdbot cron add \
  --cron "0 8 * * *" \
  --message "/root/clawd/scripts/morning-daily-summary.sh" \
  --name "Daily Morning Summary" \
  --description "每日早间资讯总结 - 8:00 AM" \
  --deliver \
  --channel feishu
```

### 晚间日报（晚上 22:00）
```bash
clawdbot cron add \
  --cron "0 22 * * *" \
  --message "/root/clawd/scripts/evening-daily-summary.sh" \
  --name "Daily Evening Summary" \
  --description "每日晚间资讯总结 - 10:00 PM" \
  --deliver \
  --channel feishu
```

## 📄 报告内容包含

### 1. 🤖 AI 资讯
- OpenClaw 相关更新
- AI 行业动态链接
- GitHub Trending

### 2. 📈 市场行情
- A股市场（上证、深证、创业板）
- 美股市场（纳斯达克、标普500、道琼斯）
- 贵金属（黄金、白银）

### 3. 💰 加密货币
- Bitcoin, Ethereum, Solana
- 实时行情链接

### 4. 🌐 Moltbook 论坛
- 观察重点和动态

### 5. 🔗 重要链接汇总
- AI Agent 平台
- 学习资源
- 开发工具

## ✅ 测试报告

已生成测试报告: `/root/clawd/reports/daily-summary-2026-02-03-21:11.md`

可以查看测试报告确认格式。

## 🔧 下一步

1. **运行 cron 添加命令**（上面提供）
2. **确认定时任务已添加**:
   ```bash
   clawdbot cron list
   ```

3. **测试手动执行**:
   ```bash
   /root/clawd/scripts/morning-daily-summary.sh
   ```

## 📝 关于 situation-monitor

**说明**: 尝试克隆 `hipcityreg/situation-monitor` 仓库时遇到网络问题。
**解决方案**: 
- 已创建自定义日报生成脚本
- 包含了各类资讯源和链接
- 可以在网络恢复后研究原仓库并集成其功能

---

*配置日期: 2026-02-03*
