# Clawdbot 可用技能完整清单

> 更新时间：2026年2月3日
> 平台：Clawdbot

---

## 📦 内置技能（Built-in Skills）

这些技能随 Clawdbot 安装，位于 `/root/.nvm/versions/node/v24.13.0/lib/node_modules/clawdbot/skills/`

### 🔧 开发与集成类

#### 1. **github** - GitHub 交互
**功能**：使用 `gh` CLI 与 GitHub 交互
- 管理 Issues 和 Pull Requests
- 检查 CI 状态和运行日志
- 高级 API 查询

**使用示例**：
```bash
gh pr checks 55 --repo owner/repo
gh run list --repo owner/repo --limit 10
gh api repos/owner/repo/pulls/55 --jq '.title, .state'
```

---

#### 2. **notion** - Notion API
**功能**：创建和管理 Notion 页面、数据库和块
- 搜索页面和数据库
- 创建/更新页面
- 查询数据库
- 添加内容块

**配置要求**：
- 需要创建 Notion Integration
- API Key 存储在 `~/.config/notion/api_key`

**使用示例**：
```bash
curl -X POST "https://api.notion.com/v1/search" \
  -H "Authorization: Bearer $NOTION_KEY" \
  -H "Notion-Version: 2025-09-03" \
  -d '{"query": "page title"}'
```

---

#### 3. **slack** - Slack 控制
**功能**：通过 `slack` 工具控制 Slack
- 消息反应（react）
- 管理 pins（固定消息）
- 发送/编辑/删除消息
- 获取成员信息

**使用场景**：
- ✅ 标记已完成任务
- 📌 固定重要决策或周报
- 👍 反应确认

---

#### 4. **skill-creator** - 技能创建工具
**功能**：创建或更新 AgentSkills
- 设计和构建技能
- 结构化技能目录
- 打包技能发布

**技能结构**：
```
skill-name/
├── SKILL.md (必需)
├── scripts/ (可执行代码)
├── references/ (文档和参考资料)
└── assets/ (模板和资源文件)
```

---

### 📱 消息与通知类

#### 5. **bluebubbles** - BlueBubbles 频道插件
**功能**：构建 BlueBubbles 外部频道插件
- REST 发送/探测
- Webhook 入站

---

#### 6. **discord** - Discord 集成
**功能**：Discord 平台集成

---

### 🔐 密码与安全类

#### 7. **1password** - 1Password 集成
**功能**：与 1Password 密码管理器集成

---

### 📝 笔记与文档类

#### 8. **apple-notes** - Apple Notes
**功能**：访问 Apple Notes

---

#### 9. **apple-reminders** - Apple Reminders
**功能**：访问 Apple Reminders

---

#### 10. **bear-notes** - Bear Notes
**功能**：访问 Bear Notes 笔记应用

---

#### 11. **obsidian** - Obsidian 笔记
**功能**：Obsidian 笔本集成

---

### 🌐 浏览与搜索类

#### 12. **bird** - Bird（Twitter/X）
**功能**：Twitter/X 集成

---

#### 13. **gog** - GOG 游戏
**功能**：GOG 游戏平台集成

---

### 🏪 本地服务类

#### 14. **food-order** - 食物订购
**功能**：订购食物相关功能

---

#### 15. **ordercli** - 订单管理
**功能**：订单管理 CLI

---

### 🗺️ 位置与地图类

#### 16. **goplaces** - Go Places
**功能**：Go Places 位置服务

---

#### 17. **local-places** - 本地位置
**功能**：本地位置服务

---

### 📧 邮件与通讯类

#### 18. **himalaya** - 邮件客户端
**功能**：Himalaya 邮件客户端集成

---

#### 19. **imsg** - iMessage
**功能**：iMessage 集成

---

### 📸 相机与媒体类

#### 20. **camsnap** - 相机快照
**功能**：相机快照功能

---

#### 21. **gifgrep** - GIF 搜索
**功能**：搜索和操作 GIF

---

#### 22. **songsee** - 音乐识别
**功能**：音乐识别和查询

---

### 🎨 创意与媒体类

#### 23. **openai-image-gen** - OpenAI 图像生成
**功能**：使用 OpenAI API 生成图像

---

#### 24. **openai-whisper** - OpenAI Whisper（本地）
**功能**：本地 Whisper 语音识别

---

#### 25. **openai-whisper-api** - OpenAI Whisper API
**功能**：使用 OpenAI Whisper API 进行语音识别

---

### 🏠 智能家居类

#### 26. **openhue** - Philips Hue
**功能**：Philips Hue 智能灯具控制

---

#### 27. **peekaboo** - 智能家居监控
**功能**：智能家居监控功能

---

### 📊 数据与分析类

#### 28. **model-usage** - 模型使用统计
**功能**：跟踪和分析模型使用情况

---

### 🤖 AI 与助手类

#### 29. **coding-agent** - 编码助手
**功能**：专门的编码代理

---

#### 30. **gemini** - Gemini 集成
**功能**：Google Gemini AI 集成

---

### 🛒 购物类

#### 31. **mcporter** - Minecraft Porter
**功能**：Minecraft 相关工具

---

### 🎮 游戏类

#### 32. **nano-banana-pro** - 游戏
**功能**：游戏相关功能

---

### 📄 文档处理类

#### 33. **nano-pdf** - PDF 处理
**功能**：PDF 文档处理

---

### 🔮 预测与 AI 类

#### 34. **oracle** - Oracle 预测
**功能**：Oracle 预测功能

---

### 🗣️ 语音与音频类

#### 35. **sag** - ElevenLabs TTS
**功能**：ElevenLabs 文本转语音
- 🎭 语音故事讲述
- 多种声音风格

---

#### 36. **sherpa-onnx-tts** - Sherpa TTS
**功能**：Sherpa ONNX 文本转语音

---

#### 37. **voice-call** - 语音通话
**功能**：语音通话功能

---

### 📋 任务与项目管理类

#### 38. **session-logs** - 会话日志
**功能**：管理和查看会话日志

---

#### 39. **summarize** - 摘要生成
**功能**：生成内容摘要

---

#### 40. **things-mac** - Things 任务管理
**功能**：Things Mac 任务管理应用

---

#### 41. **tmux** - Tmux 会话管理
**功能**：Tmux 终端复用器集成

---

#### 42. **trello** - Trello 项目管理
**功能**：Trello 看板和项目管理

---

### 🎥 视频与媒体类

#### 43. **video-frames** - 视频帧提取
**功能**：从视频中提取帧

---

### 💬 聊天与通讯类

#### 44. **wacli** - WhatsApp CLI
**功能**：WhatsApp 命令行接口

---

### 🌤️ 天气与环境类

#### 45. **weather** - 天气信息
**功能**：获取当前天气和预报（无需 API key）

**使用示例**：
- 获取当前位置天气
- 未来几天预报

---

### 🖥️ 系统与工具类

#### 46. **blucli** - Blue CLI
**功能**：Blue 命令行工具

---

#### 47. **canvas** - Canvas
**功能**：Canvas 功能

---

#### 48. **clawdhub** - ClawdHub
**功能**：ClawdHub 平台集成

---

#### 49. **sonoscli** - Sonos 控制
**功能**：Sonos 音响系统控制

---

#### 50. **spotify-player** - Spotify 播放器
**功能**：Spotify 音乐播放控制

---

---

## 🎯 工作区技能（Workspace Skills）

这些技能安装在 `/root/clawd/skills/`

### 1. **cctv-news-fetcher** - 央视新闻联播抓取
**功能**：从央视网获取《新闻联播》内容
- 支持指定日期（YYYYMMDD 格式）
- 返回 JSON 格式数据（日期、标题、内容）

**使用方法**：
```bash
node /root/clawd/skills/cctv-news-fetcher/scripts/news_crawler.js 20260202
```

**依赖**：
- `node-html-parser`（npm 包）
- Node.js 或 Bun 运行时

---

### 2. **ddg-search** - DuckDuckGo 搜索
**功能**：使用 DuckDuckGo 进行网络搜索
- 无需 API key
- 开源隐私搜索引擎

**注意**：需要安装 `jq` 工具

---

### 3. **searxng-local-search** - SearXNG 本地搜索
**功能**：使用 SearXNG 进行网络搜索
- 自托管搜索引擎
- 聚合多个搜索源

**使用场景**：
- 研究主题
- 查找文档
- 验证事实

---

### 4. **feishu-docs-publish** - 飞书文档发布
**功能**：将 Markdown 文档发布为飞书文档
- 支持本地文件读取
- 格式转换
- 文档创建/更新
- 权限设置

---

### 5. **image-generate** - 图片生成
**功能**：使用内置脚本生成图片
- 使用 `image_generate.py` 脚本
- 需要提供清晰的 prompt

---

### 6. **video- generate** - 视频生成
**功能**：使用脚本生成视频
- 使用 `video_generate.py` 脚本
- 可选首帧图片（URL 或本地路径）

---

### 7. **VeADK 技能集合** - VeADK 相关功能
**功能**：完成与 VeADK 相关的功能

---

## 🔧 系统工具（System Tools）

这些是 Clawdbot 内置的工具，不是技能：

| 工具 | 功能 |
|------|------|
| `read` | 读取文件内容 |
| `write` | 写入文件内容 |
| `edit` | 精确编辑文件 |
| `exec` | 执行 shell 命令 |
| `process` | 管理后台会话 |
| `web_search` | Brave Search API 搜索 |
| `web_fetch` | 获取网页内容 |
| `browser` | 控制浏览器 |
| `canvas` | 控制节点画布 |
| `nodes` | 节点发现和控制 |
| `cron` | 管理定时任务 |
| `message` | 发送和管理消息 |
| `gateway` | 网关管理 |
| `agents_list` | 列出可用代理 |
| `sessions_list` | 列出会话 |
| `sessions_history` | 获取会话历史 |
| `sessions_send` | 发送消息到会话 |
| `sessions_spawn` | 创建子代理会话 |
| `session_status` | 显示会话状态 |
| `memory_get` | 读取记忆片段 |
| `memory_search` | 语义搜索记忆 |
| `tts` | 文本转语音 |

---

## 💡 使用建议

### GitHub 开发者
- 使用 **github** 技能管理 Issues 和 PR
- 检查查 CI 状态
- 查看代码审查

### Notion 用户
- 使用 **notion** 技能自动化文档管理
- 查询和更新数据库
- 创建任务页面

### Slack/飞书 协作
- 使用 **slack** 技能进行消息管理
- 使用 **feishu-docs-publish** 发布文档

### 内容创作
- 使用 **image-generate** 生成配图
- 使用 **video-generate** 制作视频
- 使用 **sag** 进行语音合成

### 新闻与资讯
- 使用 **cctv-news-fetcher** 获取央视新闻
- 使用 **web_search** 搜索最新资讯

### 天气查询
- 使用 **weather** 技能获取天气（无需 API key）

---

## 📚 相关资源

- **ClawHub**: https://clawhub.com
- **Clawdbot 文档**: https://docs.clawd.bot
- **OpenClaw 文档**: https://docs.openclaw.ai
- **GitHub**: https://github.com/clawdbot/clawdbot
- **社区 Discord**: https://discord.gg/clawd

---

*文档生成时间：2026年2月3日*
*总计：50+ 内置技能 + 7 工作区技能*
