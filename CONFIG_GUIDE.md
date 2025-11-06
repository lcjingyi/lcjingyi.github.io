# 博客配置使用指南

## 概述

本博客现在使用 `blog_config.py` 文件来统一管理所有配置信息。您只需要修改这个文件，然后重新生成博客即可更新所有页面。

## 配置文件结构

### 1. 博客基本信息 (`BLOG_INFO`)
```python
BLOG_INFO = {
    "site_name": "linqixu_Blog",        # 博客名称
    "site_description": "个人技术博客",   # 博客描述
    "author": "lingqixu",               # 作者名称
    "language": "chinese (simplified)",  # 语言设置
}
```

### 2. 导航菜单配置 (`NAVIGATION_MENU`)
```python
NAVIGATION_MENU = [
    {"title": "主页", "url": "/pages/about.html"},
    {"title": "分类", "url": "/categories.html"},
    {"title": "链接", "url": "/pages/links.html"},
]
```

### 3. 关于页面内容 (`ABOUT_PAGE`)
```python
ABOUT_PAGE = {
    "title": "关于我",
    "content": """
# 关于我

欢迎来到我的个人博客！

我是一名技术爱好者，专注于软件开发、人工智能和系统架构。

在这里，我会分享我的学习笔记、技术经验和项目实践。

## 技能专长

- Python 开发
- Web 开发
- 人工智能与机器学习
- 系统架构设计

## 联系方式

- Email: your-email@example.com
- GitHub: [your-github](https://github.com/your-github)
"""
}
```

### 4. 友情链接配置 (`FRIEND_LINKS`)
```python
FRIEND_LINKS = [
    {"name": "Pelican", "url": "https://getpelican.com/", "description": "静态网站生成器"},
]
```

### 5. 社交链接配置 (`SOCIAL_LINKS`)
```python
SOCIAL_LINKS = [
    {"name": "GitHub", "url": "https://github.com/lcjingyi", "icon": "github"},

]
```

## 使用方法

### 1. 修改配置
编辑 `blog_config.py` 文件，修改相应的配置项：

```bash
# 使用您喜欢的编辑器打开配置文件
notepad blog_config.py
# 或者
code blog_config.py
```

### 2. 重新生成博客（自动同步配置）
修改配置后，直接重新生成博客，配置会自动同步：

```bash
pelican content -s pelicanconf.py
```

### 3. 预览更改
在浏览器中打开生成的页面查看更改效果。

**注意**：每次运行 `pelican content -s pelicanconf.py` 时，系统会自动：
- 同步关于页面内容
- 同步友情链接页面内容
- 应用所有配置设置

## 常见修改示例

### 修改博客名称
```python
BLOG_INFO = {
    "site_name": "我的技术博客",  # 修改这里
    # ... 其他配置
}
```

### 添加新的导航菜单项
```python
NAVIGATION_MENU = [
    {"title": "主页", "url": "/pages/about.html"},
    {"title": "分类", "url": "/categories.html"},
    {"title": "链接", "url": "/pages/links.html"},
    {"title": "归档", "url": "/archives.html"},  # 新增菜单项
]
```

### 更新关于页面内容
```python
ABOUT_PAGE = {
    "title": "关于我",
    "content": """
# 关于我

新的个人介绍内容...

## 新的技能

- 新的技能1
- 新的技能2

## 新的联系方式

- Email: new-email@example.com
- 微信: your-wechat
"""
}
```

### 添加新的友情链接
```python
FRIEND_LINKS = [
    {"name": "Pelican", "url": "https://getpelican.com/", "description": "静态网站生成器"},
    {"name": "Python.org", "url": "https://www.python.org/", "description": "Python 官方网站"},
    {"name": "Jinja2", "url": "https://palletsprojects.com/p/jinja/", "description": "模板引擎"},
    {"name": "新网站", "url": "https://newsite.com", "description": "新添加的网站"},  # 新增链接
]
```

## 注意事项

1. **修改后必须重新生成**：修改 `blog_config.py` 后必须运行 `pelican content -s pelicanconf.py` 才能生效

2. **URL 路径**：导航菜单中的 URL 路径需要与实际的页面路径一致

3. **Markdown 格式**：关于页面内容使用 Markdown 格式编写

4. **备份配置**：建议定期备份您的配置文件

## 故障排除

如果修改配置后出现问题：

1. 检查 Python 语法是否正确
2. 确保所有引号和括号都正确闭合
3. 检查 URL 路径是否正确
4. 查看 Pelican 生成时的错误信息

## 高级配置

如需更高级的配置，可以修改 `pelicanconf.py` 文件中的其他设置，或参考 Pelican 官方文档。

---

*如有问题，请查看 Pelican 官方文档或联系开发者*