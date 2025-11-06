# linqixu_Blog

个人博客项目，使用 Pelican 静态网站生成器。

## 快速开始

### 修改博客配置
编辑 `blog_config.py` 文件来更新博客的所有信息：
- 博客名称和描述
- 导航菜单
- 关于页面内容
- 友情链接
- 社交链接

### 生成博客
```bash
pelican content -s pelicanconf.py
```

**注意**：每次生成博客时，配置会自动同步到相关页面。

### 查看详细说明
查看 `CONFIG_GUIDE.md` 了解完整的配置说明。

---

## 常用命令

```bash
# 生成博客
python -m pelican content -s pelicanconf.py
# 本地预览
python -m pelican --listen

# 部署到 GitHub Pages
ghp-import -n -p output/
``` 