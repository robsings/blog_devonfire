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

AUTHOR = 'rob.sings'
SITENAME = ' Blog DevOnFire - Artigos, códigos e devaneios '
SITEDESCRIPTION = 'O humilde legado digital de um dev em chamas | Estudos, códigos e conversas sobre os mais variados assuntos — da tecnologia e seus rumos à cultura nerd/geek.'
SITEURL = ""
SITELOGO='https://devonfire.blog/theme/images/logo2.png'

PATH = "content"
ARTICLE_ORDER_BY = 'date'
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%d %B %Y'
#PATH_METADATA = './content/Extra/.*'
TIMEZONE = 'America/Sao_Paulo'
PLUGIN_PATHS = ['pelican-plugins']
# Aqui no plugins anteriormente só havia o neighbors
PLUGINS = ['neighbors', 'sitemap', 'related_posts','archive_menu_generator']

DEFAULT_LANG = 'en' #'en'

THEME = "./tema/"

STATIC_PATHS = ['images', 'extra/robots.txt']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
}
DEFAULT_METADATA = {
    'meta_description': SITEDESCRIPTION,
    'seo_keywords': 'blog, devonfire, tecnologia, programação, rob.sings, @rob.sings, Robsings, robsings, rob_sings, dev, nerd, geek',
    'seo_author': 'Roberto Santos, @rob.sings, @Robsings_, rob.sings, robsings',
}
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
    ("X", "https://x.com/Robsings_"),
    ("Medium","https://medium.com/@rob.sings")
)
READERS={
    'html':None,
}
# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)
MARKDOWN = {
    'extensions': ['codehilite', 'extra','fenced_code'],
    'extension_configs': {
        'codehilite': {
            'css_class': 'highlight',
            'linenums':False,
            'guess_lang': False,
            'use_pygments': True
            },
    },
    'output_format': 'html5',
}
PYGMENTS_STYLE = 'monokai'
SITEMAP = {
    'format': 'xml',
    'priorities':{
        'articles':0.7,
        'pages':0.5,
        'indexes':0.1

    },
    'changefreqs': {
        'articles': 'weekly',  # Posts podem ser atualizados semanalmente
        'pages': 'monthly',    # Páginas mudam menos
        'indexes': 'monthly',
    }
}

DEFAULT_ORPHANS = 0

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
