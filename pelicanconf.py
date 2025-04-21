import sys
import os
from datetime import datetime
from jinja2 import Environment

sys.path.append(os.path.join(os.path.dirname(__file__), 'pelican-plugins'))

def month_name(month_number):
    return datetime(1900, month_number, 1).strftime('%B')

JINJA_FILTERS = {
    'month_name': month_name,
}
SITEYEAR = datetime.now().year

AUTHOR = '@Robsings'
SITENAME = ' Blog DevOnFire - O humilde legado digital de um dev em chamas | Artigos, códigos e devaneios '
SITEURL = ""

PATH = "content"
ARTICLE_ORDER_BY = 'date'
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%d %B %Y'

TIMEZONE = 'America/Sao_Paulo'
PLUGIN_PATHS = ['pelican-plugins']
# Aqui no plugins anteriormente só havia o neighbors
PLUGINS = ['neighbors', 'sitemap', 'related_posts','archive_menu_generator']

DEFAULT_LANG = 'en'

THEME = "./tema/"
STATIC_PATHS = ['images']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
EXTRA_PATH_METADATA = {
    './extra/robots.txt': {'path': 'robots.txt'},
}
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
SITEMAP = {
    'format': 'xml',
}

DEFAULT_ORPHANS = 0

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
