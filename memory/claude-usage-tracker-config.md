# Claude Code Usage Tracker - 配置说明

## ✅ 已完成的安装

### 安装的脚本
1. **claude-usage.sh** - 检查 Claude Code 使用限制
2. **session-reminder.sh** - 会话重置提醒
3. **monitor-usage.sh** - 使用监控和重置检测
4. **setup-monitoring.sh** - 设置监控的自动化脚本

所有脚本已复制到 `/root/clawd/scripts/` 并设置了执行权限。

## ⚠️ 当前限制

### 问题
1. **Claude CLI 未安装** - 需要先安装 Claude Code CLI
2. **凭证存储** - Linux 环境需要 `secret-tool` 或安装 Claude CLI
3. **无 OAuth 凭证** - 需要先运行 Claude CLI 进行认证

## 🔧 解决方案

### 方案 A：安装 Claude Code CLI（推荐）

```bash
# 安装 Claude CLI
npm install -g @anthropic-ai/claude-code

# 运行一次以触发 OAuth 认证
claude "hello"
```

### 方案 B：安装 secret-tool（Linux）

```bash
# Debian/Ubuntu
sudo apt update && sudo apt install -y libsecret-tools

# Fedora/RHEL
sudo dnf install -y libsecret
```

## 🚀 完成配置后的使用

### 手动检查使用情况
```bash
# 查看使用情况（使用缓存）
/root/clawd/scripts/claude-usage.sh

# 强制刷新
/root/clawd/scripts/claude-usage.sh --fresh

# JSON 输出
/root/clawd/scripts/claude-usage.sh --json
```

### 设置自动提醒（推荐）

安装 Claude CLI 后运行：
```bash
# 设置会话重置提醒
/root/clawd/scripts/session-reminder.sh
```

这将创建一个自动调度的 cron 任务，在每次会话配额重置时发送提醒。

### 设置监控（替代方案）

```bash
# 初始化监控
/root/clawd/scripts/monitor-usage.sh

# 设置定时监控（每30分钟）
# 需要通过 Clawdbot cron 设置
```

## 📊 预期输出示例

### 文本格式
```
🦞 Claude Code Usage

⏱️  Session (5h): 🟢 ████░░░░░░ 40%
   Resets in: 2h 15m

📅 Weekly (7d): 🟡 ██████░░░░ 60%
   Resets in: 3d 8h
```

### JSON 格式
```json
{
  "session": {
    "utilization": 40,
    "resets_in": "2h 15m",
    "resets_at": "2026-01-19T22:15:00Z"
  },
  "weekly": {
    "utilization": 60,
    "resets_in": "3d 8h",
    "resets_at": "2026-01-22T04:00:00Z"
  },
  "cached_at": "2026-01-19T20:00:00Z"
}
```

## 📝 下一步

1. **安装 Claude Code CLI**
   ```bash
   npm install -g @anthropic-ai/claude-code
   ```

2. **认证 Claude CLI**
   ```bash
   claude "hello"
   ```

3. **测试脚本**
   ```bash
   /root/clawdud/scripts/claude-usage.sh --fresh
   ```

4. **设置自动提醒**
   ```bash
   /root/clawd/scripts/session-reminder.sh
   ```

## 💡 备注

- 脚本使用系统密钥链存储 OAuth 凭证（macOS）或 secret-tool（Linux）
- 智能缓存：默认 60 秒缓存，避免频繁 API 调用
- 自动 token 刷新：如果 OAuth token 过期，会自动触发刷新
- 支持多个监控方法，建议使用 session-reminder.sh 进行精确提醒

---

*配置日期：2026-02-03*
*状态：脚本已安装，等待 Claude CLI 安装*
