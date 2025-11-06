#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
博客配置文件
每次修改此文件后，重新生成博客即可更新所有页面
"""

# ==================== 博客基本信息 ====================
BLOG_INFO = {
    "site_name": "linqixu_Blog",
    "site_description": "个人技术博客",
    "author": "lingqixu",
    "language": "chinese (simplified)",
}

# ==================== 导航菜单配置 ====================
NAVIGATION_MENU = [
    {"title": "主页", "url": "/"},
    {"title": "分类", "url": "/categories.html"},
    {"title": "链接", "url": "/pages/links.html"},
]

# ==================== 关于页面内容 ====================
ABOUT_PAGE = {
    "title": "关于我",
    "content": """
# 关于我

欢迎来到我的个人博客！

我是一名技术爱好者，专注于软件开发、人工智能和系统架构。

在这里，我会分享我的学习笔记、技术经验和项目实践。

## 技能专长

- Python 开发
- 渗透测试
- 工具开发

## 联系方式

- Email: 
- GitHub: [lcjingyi](https://github.com/lcjingyi)
"""
}

# ==================== 友情链接配置 ====================
FRIEND_LINKS = [
    {"name": "Pelican", "url": "https://getpelican.com/", "description": "静态网站生成器"},
]

# ==================== 社交链接配置 ====================
SOCIAL_LINKS = [
    {"name": "GitHub", "url": "https://github.com/your-github", "icon": "github"},
]

# ==================== 主题配置 ====================
THEME_CONFIG = {
    "theme_name": "minimal",
    "css_variables": {
        "primary_color": "#2c3e50",
        "secondary_color": "#3498db",
        "accent_color": "#e74c3c",
        "text_color": "#333",
        "bg_color": "#fff",
    }
}

# ==================== 生成配置的函数 ====================
def generate_pelican_config():
    """
    生成 Pelican 配置字典
    在 pelicanconf.py 中调用此函数
    """
    config = {
        # 博客基本信息
        'SITENAME': BLOG_INFO['site_name'],
        'SITEURL': '',
        'AUTHOR': BLOG_INFO['author'],
        'DEFAULT_LANG': BLOG_INFO['language'],

        # 路径设置
        'PATH': 'content',
        'STATIC_PATHS': ['images'],
        'ARTICLE_PATHS': [''],
        'PAGE_PATHS': ['pages'],

        # 时区设置
        'TIMEZONE': 'Asia/Shanghai',
        'DEFAULT_DATE': 'fs',

        # 主题设置
        'THEME': 'themes/minimal',

        # 分页设置
        'DEFAULT_PAGINATION': 10,
        'PAGINATION_PATTERNS': (
            (1, '{base_name}/', '{base_name}/index.html'),
            (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
        ),

        # Feed 设置
        'FEED_ALL_ATOM': None,
        'CATEGORY_FEED_ATOM': None,
        'TRANSLATION_FEED_ATOM': None,
        'AUTHOR_FEED_ATOM': None,
        'AUTHOR_FEED_RSS': None,

        # 插件设置
        'PLUGIN_PATHS': ['plugins'],
        'PLUGINS': [],

        # 菜单显示设置
        'DISPLAY_PAGES_ON_MENU': False,
        'DISPLAY_CATEGORIES_ON_MENU': False,
    }

    return config


def get_navigation_context():
    """
    获取导航菜单的上下文数据
    在模板中使用
    """
    return {
        'navigation_menu': NAVIGATION_MENU,
        'friend_links': FRIEND_LINKS,
        'social_links': SOCIAL_LINKS,
    }


if __name__ == "__main__":
    # 测试配置
    print("博客配置测试:")
    print(f"站点名称: {BLOG_INFO['site_name']}")
    print(f"作者: {BLOG_INFO['author']}")
    print(f"导航菜单: {[item['title'] for item in NAVIGATION_MENU]}")
    print(f"友情链接数量: {len(FRIEND_LINKS)}")
    print(f"社交链接数量: {len(SOCIAL_LINKS)}")