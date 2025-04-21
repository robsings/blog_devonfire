from datetime import datetime
SITEYEAR = datetime.now().year

AUTHOR = '@Robsings'
SITENAME = ' Blog DevOnFire - O humilde legado digital de um dev em chamas | Artigos, códigos e devaneios '
SITEURL = ""

PATH = "content"
ARTICLE_ORDER_BY = 'date'

TIMEZONE = 'America/Sao_Paulo'
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['neighbors']

DEFAULT_LANG = 'en'

THEME = "./tema/"
STATIC_PATHS = ['images']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LOAD_CONTENT_CACHE = False

# Blogroll
LINKS = (
    ("GitHub", "https://github.com/robsings"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)
MARKDOWN = {
    'extensions': ['codehilite', 'extra'],
    'extension_configs': {
        'codehilite': {'css_class': 'highlight'},
    },
    'output_format': 'html5',
}

DEFAULT_ORPHANS = 0

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
