# GitHub 记忆上传指南

## 📋 当前状态

✅ GitHub CLI 已安装（版本 2.23.0）
❌ 尚未登录 GitHub

## 🔑 认证方式

您可以选择以下任一方式进行 GitHub 认证：

### 方式 1：使用 GitHub Token（推荐）

1. **创建 GitHub Personal Access Token**：
   - 访问：https://github.com/settings/tokens
   - 点击 "Generate new token" → "Generate new token (classic)"
   - 设置 token 描述（如：Clawdbot Memory Upload）
   - 选择权限：
     - ✅ `repo`（完整仓库访问权限）
     - ✅ `workflow`（如果需要运行 GitHub Actions）
   - 点击生成并复制 token

2. **配置 Token**：
   ```bash
   export GITHUB_TOKEN=your_token_here
   ```

3. **验证登录**：
   ```bash
   /usr/bin/gh auth status
   ```

### 方式 2：使用 GitHub App 认证

在本地终端运行：
```bash
/usr/bin/gh auth login
```

然后选择浏览器认证流程。

## 📤 上传记忆文件

一旦认证成功，可以执行以下操作：

### 选项 A：推送到现有仓库

```bash
cd /root/clawd
git init
git add memory/ MEMORY.md
git commit -m "Upload Clawdbot memory files"
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

### 选项 B：创建新仓库并推送

```bash
# 创建新仓库
/usr/bin/gh repo create clawdbot-memory --public --description "Clawdbot Agent Memory Files"

# 初始化 git
cd /root/clawd
git init
git add memory/ MEMORY.md
git commit -m "Initial commit: Upload Clawdbot memory files"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/clawdbot-memory.git
git push -u origin main
```

## 📁 将要上传的文件

### 核心记忆文件
- `MEMORY.md` - 长期记忆
- `memory/` 目录 - 每日记忆文件

### 学习文档
- `skills-learning-summary.md` - Skills 学习总结
- `skills-complete-list.md` - 完整技能清单

### 项目配置文件
- `SOUL.md` - Agent 身份和个性
- `USER.md` - 用户信息
- `AGENTS.md` - Agent 配置
- `TOOLS.md` - 工具配置

## 🎯 下一步

请提供以下信息之一：

1. **GitHub Token** - 我可以直接配置并执行上传
2. **现有仓库 URL** - 如果已有仓库，可以推送到那里
3. **新仓库名称** - 创建新仓库并推送

---

*提示：Token 只会保存在当前会话中，不会写入文件*
