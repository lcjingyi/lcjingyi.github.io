# 导入自定义配置
from blog_config import generate_pelican_config, get_navigation_context

# 使用自定义配置
config = generate_pelican_config()

# 设置配置变量
AUTHOR = config['AUTHOR']
SITENAME = config['SITENAME']
SITEURL = config['SITEURL']
PATH = config['PATH']
TIMEZONE = config['TIMEZONE']
DEFAULT_LANG = config['DEFAULT_LANG']
THEME = config['THEME']
STATIC_PATHS = config['STATIC_PATHS']
ARTICLE_PATHS = config['ARTICLE_PATHS']
PAGE_PATHS = config['PAGE_PATHS']
DEFAULT_DATE = config['DEFAULT_DATE']
DEFAULT_PAGINATION = config['DEFAULT_PAGINATION']
PAGINATION_PATTERNS = config['PAGINATION_PATTERNS']
FEED_ALL_ATOM = config['FEED_ALL_ATOM']
CATEGORY_FEED_ATOM = config['CATEGORY_FEED_ATOM']
TRANSLATION_FEED_ATOM = config['TRANSLATION_FEED_ATOM']
AUTHOR_FEED_ATOM = config['AUTHOR_FEED_ATOM']
AUTHOR_FEED_RSS = config['AUTHOR_FEED_RSS']
PLUGIN_PATHS = config['PLUGIN_PATHS']
PLUGINS = config['PLUGINS']
DISPLAY_PAGES_ON_MENU = config['DISPLAY_PAGES_ON_MENU']
DISPLAY_CATEGORIES_ON_MENU = config['DISPLAY_CATEGORIES_ON_MENU']

# 导航菜单上下文
NAVIGATION_CONTEXT = get_navigation_context()

# 分类设置
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORY_URL = 'category/{slug}/'

# 标签设置
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAG_URL = 'tag/{slug}/'

# 作者设置
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHOR_URL = 'author/{slug}/'
