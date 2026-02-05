# 📊 Claude Code Usage Tracker - 安装完成

## ✅ 已完成

1. **安装脚本** - 4个监控脚本已复制到 `/root/clawd/scripts/`
   - `claude-usage.sh` - 检查使用情况
   - `session-reminder.sh` - 会话重置提醒
   - `monitor-usage.sh` - 使用监控
   - `setup-monitoring.sh` - 自动设置监控

2. **设置权限** - 所有脚本已设置执行权限

3. **创建文档** - 详细配置文档已保存

## ⚠️ 需要完成

### Claude CLI 未安装

要使用这些脚本，需要先安装 Claude Code CLI：

```bash
# 安装
npm install -g @anthropic-ai/claude-code

# 认证（会打开浏览器进行 OAuth）
claude "hello"

# 测试脚本
/root/clawd/scripts/claude-usage.sh --fresh
```

### 安装 Claude CLI 后

运行以下命令启用自动提醒：

```bash
# 设置会话重置提醒（推荐）
/root/clawd/scripts/session-reminder.sh
```

这将在每次 5 小时会话配额重置时发送提醒通知。

## 📄 详细文档

完整配置说明已保存到：
`/root/clawd/memory/claude-usage-tracker-config.md`

## 🎯 功能预览

安装完成后，你将获得：

- 📊 **实时使用监控** - 查看会话和周使用情况
- 🔄 **自动重置提醒** - 配额重置时自动通知
- ⚡ **智能缓存** - 60秒缓存避免频繁API调用
- 🎨 **美观输出** - 进度条、emoji、颜色编码

需要我帮你安装 Claude CLI 吗？
