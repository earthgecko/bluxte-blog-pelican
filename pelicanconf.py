# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import glob
import hashlib
import sys
from os import path

# PUBLISH is set to True in publishconf.py. This allows having variations 
# between edit and publish modes in a single location
sys.path.append(path.join('..', 'engine'))
from pelicanglobals import PUBLISH

print ("Conf - PUBLISH = {}".format(PUBLISH))

AUTHOR = 'Sylvain Wallez'
SITENAME = 'Sylvain Wallez'
SITESUBTITLE = 'Random musings of a busy geek'
SITEURL = ''

BASE_PATH = '..'
PATH = 'content'
ENGINE_PATH = BASE_PATH + "/engine"

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'en'

# System
CACHE_CONTENT = True

if PUBLISH:
    PLUGIN_PATHS = [ENGINE_PATH + "/plugins"]
else:
    PLUGIN_PATHS = [ENGINE_PATH + "/plugins", BASE_PATH + "/pelican-plugins"]

PLUGINS = ["assets", "neighbors"]

# ---------- Feeds

if PUBLISH:
    FEED_ALL_RSS = 'index.xml'
else:
    FEED_ALL_RSS = None

FEED_ALL_ATOM = None
FEED_RSS = None
FEED_ATOM = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
FEED_MAX_ITEMS = 10

# ---------- Theme and menu

THEME = ENGINE_PATH + '/themes/clean-blog'

# Some other themes I liked
#THEME = '../pelican-themes/flex'
#THEME = '../pelican-themes/pure'
#THEME = '../pelican-themes/hyde'

# ---------- Menu

MENUITEMS = (
    ('About', '/about/'),
    ('Archives', '/musings/'),)

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

# ---------- Social

# For opengraph and twitter cards meta headers
FB_USERNAME = 'sylvain.wallez'
TWITTER_USERNAME = 'bluxte'

# Social widget
SOCIAL = (
    ('twitter', 'https://twitter.com/bluxte'),
    ('linkedin', 'https://www.linkedin.com/in/swallez'),
    ('github', 'https://github.com/swallez'),
    ('slideshare', 'http://www.slideshare.net/swallez'),
    ('facebook', 'https://www.facebook.com/' + FB_USERNAME),
    # ('rss', '/' + FEED_ALL_RSS),
)

SHOW_SOCIAL_ON_INDEX_PAGE_HEADER = True

# ---------- Misc settings

DEFAULT_PAGINATION = 10

USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = 'misc'

DIRECT_TEMPLATES = ['index', 'archives'] # Leaving out 'tags', 'categories', 'authors'
PAGINATED_DIRECT_TEMPLATES = ['index']

#SUMMARY_MAX_LENGTH = 50
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# ---------- Content paths ad URLs

SLUGIFY_SOURCE = 'basename' # basename or title

ARTICLE_PATHS = ['musings']
ARTICLE_URL = 'musings/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'musings/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

PAGE_PATHS = ['pages']

STATIC_PATHS = [
    'musings', # I love attachments to be close to content
    'images',
    'extra', # Stuff to copy at the site root (must be listed in extra path below)
    'archives' # Contains old posts images (will moved to 'musings' alongside their respective posts)
]

# Would love to be have regexps or at least prefix patching
# (see also using the Makefile https://github.com/getpelican/pelican/wiki/Tips-n-Tricks )
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

# ---------- Archives

if PUBLISH:
    ARCHIVES_SAVE_AS = 'musings/index.html'
    YEAR_ARCHIVE_SAVE_AS = 'musings/{date:%Y}/index.html'
    MONTH_ARCHIVE_SAVE_AS = 'musings/{date:%Y}/{date:%m}/index.html'
    DAY_ARCHIVE_SAVE_AS = 'musings/{date:%Y}/{date:%m}/{date:%d}/index.html'
else:
    # Don't spend time generating those in edit mode
    ARCHIVES_SAVE_AS = ''
    YEAR_ARCHIVE_SAVE_AS = ''
    MONTH_ARCHIVE_SAVE_AS = ''
    DAY_ARCHIVE_SAVE_AS = ''

# ----------

ISSO_SERVER = 'http://localhost:8080'

JINJA_FILTERS = {}

COLOR_SCHEME_CSS = 'github.css'

# Random banner images.
# If a post doesn't specify a banner image, one is selected randomly from those in
# the images/banners directory. To ensure the image is the same every time we pubish,
# 'random' is computed from the page's URL using MD5(url) % nb_banners
# All banners will change if we add/remove pictures, but this is fine.

banner_images = [f.replace(PATH + "/", "") for f in glob.glob(PATH + "/images/banners/*.jpg")]
banner_images.sort()

def random_banner(url):
    hash = int(hashlib.md5(url.encode('utf-8')).hexdigest(), 16)
    return banner_images[hash % len(banner_images)]

JINJA_FILTERS['random_banner'] = random_banner
