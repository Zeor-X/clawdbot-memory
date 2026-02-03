# ClawHub Skills 学习总结

> 学习时间：2026年2月3日
> 平台：skills.sh / clawhub.com

---

## 📚 什么是 Skills

**Skills（技能）** 是为 AI Agent 添加可重用能力的方式。技能是包含 `SKILL.md` 文件的文件夹，用于教 Agent 如何执行特定任务。

### 核心特点
- ✅ **单一命令安装**：一条命令即可增强 Agent 能力
- ✅ **可重用知识**： procedural knowledge（程序性知识）
- ✅ **公共注册表**：免费、开放、可见的技能共享平台
- ✅ **版本管理**：semver 版本控制，支持更新和回退

---

## 🌐 ClawHub 生态

### 网站
- **主站**：https://clawhub.com
- **文档**：https://docs.openclaw.ai/tools/skills
- **GitHub**：https://github.com/openclaw/skills

### 技能来源优先级
```
<workspace>/skills (最高优先级)
    ↓
~/.openclaw/skills (本地管理)
    ↓
bundled skills (内置技能)
    ↓
skills.load.extraDirs (配置的额外目录)
```

### 安装位置
默认安装到当前工作目录的 `./skills/` 或配置的 OpenClaw workspace。

---

## 🛠️ CLI 工具安装

### 安装 clawhub CLI

```bash
# 使用 npm
npm install -g clawhub

# 使用 pnpm
pnpm add -g clawhub
```

### 常用命令

| 命令 | 说明 |
|------|------|
| `clawhub login` | 登录（浏览器流程） |
| `clawhub login --token <token>` | 使用 token 登录 |
| `clawhub logout` | 登出 |
| `clawhub whoami` | 查看当前用户 |
| `clawhub search "query"` | 搜索技能 |
| `clawhub install <slug>` | 安装技能 |
| `clawhub update <slug>` | 更新指定技能 |
| `clawhub update --all` | 更新所有技能 |
| `clawhub list` | 列出已安装技能 |
| `clawhub publish <path>` | 发布技能 |

### 全局选项

- `--workdir <dir>` - 工作目录
- `--dir <dir>` - 技能目录（默认 skills）
- `--site <url>` - 网站 URL
- `--registry <url>` - 注册表 API URL
- `--no-input` - 非交互模式

---

## 📄 技能格式规范

### SKILL.md 基本结构

```markdown
---
name: skill-name
description: Brief description of what this skill does
metadata:
  openclaw:
    requires:
      bins: ["command1", "command2"]
      env: ["API_KEY_NAME"]
    emoji: "🎯"
---

# 技能标题

这里写详细的技能说明和使用指南。

## 使用方法

描述如何使用这个技能...

## 配置

列出需要的配置项...

## 示例

提供使用示例...
```

### 必需字段

- `name` - 技能名称
- `description` - 技能描述

### 可选 frontmatter 字段

| 字段 | 说明 |
|------|------|
| `homepage` | 技能网站 URL |
| `user-invocable` | 是否作为用户斜杠命令暴露（默认 true） |
| `disable-model-invocation` | 是否从模型提示中排除（默认 false） |
| `command-dispatch` | 设置为 `tool` 时跳过模型直接调用工具 |
| `command-tool` | 工具名称 |
| `command-arg-mode` | 参数传递模式（默认 raw） |

### Metadata（元数据）

```json
{
  "openclaw": {
    "always": true,           // 始终包含（跳过其他过滤）
    "emoji": "🎯",            // macOS Skills UI 显示的图标
    "homepage": "https://...", // 网站链接
    "os": ["darwin", "linux"], // 支持的操作系统
    "requires": {
      "bins": ["uv", "jq"],            // 必需的二进制文件
      "anyBins": ["docker", "podman"], // 至少一个必需
      "env": ["GEMINI_API_KEY"],        // 必需的环境变量
      "config": ["browser.enabled"]      // 必需的配置项
    },
    "primaryEnv": "GEMINI_API_KEY",     // 主要环境变量
    "install": [...]                     // 安装说明
  }
}
```

---

## 🎯 实践案例

### 案例 1：安装搜索技能

```bash
# 搜索相关技能
clawhub search "search"

# 安装 DuckDuckGo 搜索技能
clawhub install ddg-search

# 安装 SearXNG 本地搜索技能
clawhub install searxng-local-search

# 安装 CCTV 新闻抓取技能
clawhub install cctv-news-fetcher
```

### 案例 2：CCTV 新闻抓取技能

**技能位置**：`/root/clawd/skills/cctv-news-fetcher`

**使用方法**：
```bash
# 获取指定日期的新闻联播内容（格式 YYYYMMDD）
node /root/clawd/skills/cctv-news-fetcher/scripts/news_crawler.js 20260202
```

**返回格式**：JSON 数组，包含日期、标题、内容

**依赖**：
- `node-html-parser`（npm 包）
- `bun` 或 `node` 运行时

---

## 🔒 安全注意事项

### ⚠️ 重要原则

1. **第三方技能不可信**
   - 安装前阅读技能代码
   - 了解技能的运行方式

2. **沙箱运行**
   - 对不受信任的输入和风险工具使用沙箱
   - 避免直接执行未知命令

3. **密钥管理**
   - `skills.entries.*.env` 和 `skills.entries.*.apiKey` 会将密钥注入进程
   - **不要**在提示或日志中包含密钥
   - 使用环境变量或配置文件管理密钥

4. **报告和审核**
   - 发现滥用技能可以举报
   - 技能收到3个以上举报会自动隐藏
   - 管理员可以隐藏、取消隐藏、删除或封禁用户

---

## 📖 技能系统概述

### 技能包含什么

- `SKILL.md` - 主说明和用法
- 可选配置文件
- 脚本或支持文件
- 元数据（标签、摘要、安装要求）

### 元数据作用

- **发现** - 通过名称、标签、搜索查找
- **过滤** - 根据环境、配置、二进制存在性加载技能
- **安全** - 限制技能的暴露和调用
- **排名** - 使用信号（stars、downloads）改进搜索结果

---

## 🚀 高级用法

### 发布技能

```bash
# 发布本地技能
clawhub publish /path/to/skill-directory

# 指定 slug
clawhub publish /path/to/skill-dir --slug my-custom-skill
```

### 同步技能

```bash
# 扫描本地技能并发布更新
clawhub sync --all

# 同步指定技能
clawhub sync my-skill
```

### 版本管理

```bash
# 安装特定版本
clawhub install skill-name --version 1.2.0

# 更新到特定版本
clawhub update skill-name --version 2.0.0
```

---

## 💡 最佳实践

### 1. 技能设计

- ✅ 保持 `SKILL.md` 清晰简洁
- ✅ 提供详细的使用示例
- ✅ 说明依赖和配置要求
- ✅ 包含故障排查指南

### 2. 发布前检查

- ✅ 测试所有脚本
- ✅ 验证元数据格式正确
- ✅ 检查依赖是否列出
- ✅ 确保没有硬编码密钥

### 3. 版本控制

- ✅ 遵循 semver 规范
- ✅ 记录变更日志
- ✅ 测试兼容性

### 4. 社区互动

- ✅ 响应用户反馈
- ✅ 及时修复问题
- ✅ 更新文档

---

## 📚 相关资源

- **OpenClaw 官网**：https://docs.openclaw.ai
- **技能文档**：https://docs.openclaw.ai/tools/skills
- **ClawHub**：https://clawhub.com
- **AgentSkills 规范**：兼容 AgentSkills 规范
- **社区 Discord**：https://discord.gg/clawd

---

## ✅ 学习成果

通过这次学习，我掌握了：

1. ✅ **ClawHub CLI** 的安装和使用
2. ✅ **搜索和安装技能** 的方法
3. ✅ **SKILL.md 格式规范** 和元数据配置
4. ✅ **技能优先级和加载机制**
5. ✅ **安全注意事项** 和最佳实践
6. ✅ **实际技能安装**（ddg-search、searxng-local-search、cctv-news-fetcher）
7. ✅ **CCTV 新闻抓取** 的成功实践

---

*文档生成时间：2026年2月3日*
*生成者：Clawdbot Agent*
