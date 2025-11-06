#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
配置同步脚本
在生成博客前运行此脚本，将配置中的内容同步到相应的页面文件
"""

import os
import sys

# 添加当前目录到路径，以便导入 blog_config
sys.path.append(os.path.dirname(__file__))

from blog_config import ABOUT_PAGE, FRIEND_LINKS, SOCIAL_LINKS

def sync_about_page():
    """同步关于页面内容"""
    about_file_path = os.path.join("content", "pages", "about.md")

    # 读取现有的关于页面文件
    if os.path.exists(about_file_path):
        with open(about_file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # 找到内容开始的位置（第一个空行之后）
        content_start = 0
        for i, line in enumerate(lines):
            if line.strip() == '':
                content_start = i + 1
                break

        # 保留元数据部分，替换内容部分
        metadata = lines[:content_start]
        new_content = ABOUT_PAGE["content"]

        # 写入新文件
        with open(about_file_path, 'w', encoding='utf-8') as f:
            f.writelines(metadata)
            f.write(new_content)

        print(f"[SYNC] 已同步关于页面: {about_file_path}")
    else:
        print(f"[ERROR] 关于页面文件不存在: {about_file_path}")


def sync_links_page():
    """同步友情链接页面内容"""
    links_file_path = os.path.join("content", "pages", "links.md")

    # 生成友情链接的 Markdown 内容
    links_content = """# 友情链接

## 技术相关

### 开发工具
"""

    # 添加友情链接
    for link in FRIEND_LINKS:
        links_content += f"- [{link['name']}]({link['url']}) - {link['description']}\n"

    links_content += """
## 社交链接

### 我的社交账号
"""

    # 添加社交链接
    for link in SOCIAL_LINKS:
        links_content += f"- [{link['name']}]({link['url']})\n"

    # 读取现有的链接页面文件
    if os.path.exists(links_file_path):
        with open(links_file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # 找到内容开始的位置（第一个空行之后）
        content_start = 0
        for i, line in enumerate(lines):
            if line.strip() == '':
                content_start = i + 1
                break

        # 保留元数据部分，替换内容部分
        metadata = lines[:content_start]

        # 写入新文件
        with open(links_file_path, 'w', encoding='utf-8') as f:
            f.writelines(metadata)
            f.write(links_content)

        print(f"[SYNC] 已同步链接页面: {links_file_path}")
    else:
        print(f"[ERROR] 链接页面文件不存在: {links_file_path}")


def sync_all_config():
    """同步所有配置"""
    print("=== 开始同步配置 ===")
    sync_about_page()
    sync_links_page()
    print("=== 配置同步完成 ===")


if __name__ == "__main__":
    sync_all_config()