# Coder Style Theme for Pelican

一个类似Hexo Coder主题的博客主题，专为Pelican静态网站生成器设计。

## 特性

- **Coder风格设计**: 类似Hexo Coder主题的现代简约风格
- **侧边栏布局**: 左侧导航栏，右侧内容区域
- **响应式**: 在桌面和移动设备上都能完美显示
- **文章摘要**: 首页只显示文章标题和摘要
- **现代化代码高亮**: 深色主题的代码块显示
- **易定制**: 使用CSS变量，便于自定义颜色和间距
- **无障碍**: 符合无障碍设计标准

## 安装

1. 将主题文件夹复制到您的Pelican项目的`themes/`目录下
2. 在`pelicanconf.py`中设置主题：
   ```python
   THEME = "themes/minimal"
   ```

## 自定义

### 颜色主题

主题使用CSS变量，您可以通过覆盖这些变量来自定义外观：

```css
:root {
    --primary-color: #2c3e50;    /* 主要颜色 */
    --secondary-color: #3498db;  /* 次要颜色 */
    --accent-color: #e74c3c;     /* 强调色 */
    --text-color: #333;          /* 文本颜色 */
    --bg-color: #fff;            /* 背景颜色 */
}
```

### 布局

- 最大宽度：800px
- 响应式断点：768px 和 480px
- 使用CSS Grid 和 Flexbox 布局

## 模板

主题包含以下模板：

- `base.html` - 基础模板
- `index.html` - 首页模板
- `article.html` - 文章页面模板
- `page.html` - 页面模板
- `archives.html` - 归档页面模板
- `categories.html` - 分类页面模板
- `tags.html` - 标签页面模板

## 浏览器支持

- Chrome (最新)
- Firefox (最新)
- Safari (最新)
- Edge (最新)

## 许可证

MIT License

## 贡献

欢迎提交问题和拉取请求来改进这个主题。