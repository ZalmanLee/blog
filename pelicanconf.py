#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'ZalmanLee'
SITENAME = u"zalman's blog"
SITEURL = 'https://blog.0x7c00.me'

PATH = 'content'

STATIC_PATHS = [
    'static',
    'extra/robots.txt',
    'extra/favicon.ico',
]
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh_CN'

THEME = 'theme/waterspill'

CNZZ_ANALYTICS = True

USE_ISSO = True

# Feed generation is usually not desired when developing
FEED_ATOM = 'feeds/atom.xml'
FEED_RSS = 'feeds/rss.xml'

LINKS = (("灰色地带", "http://ev1l.cn/"),
         ("Onioner", "http://onioner.com/"),)

# Social widget
SOCIAL = (("weibo", "http://weibo.com/zalmanlee"),)

DEFAULT_PAGINATION = 10

USE_FOLDER_AS_CATEGORY = True

DISPLAY_PAGES_ON_MENU = True

RELATIVE_URLS = True

PLUGIN_PATHS = ['plugins']

PLUGINS = [
    'gzip_cache',
    'neighbors',
    'sitemap',
    'always_modified',
    'md_prism_highlight'
]

SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.7,
        "indexes": 0.5,
        "pages": 0.3,
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly",
    }
}

ALWAYS_MODIFIED = True

PRISM_PRESET = {
    'mypreset': {
        'lineno': True,
        'line': '1-4,7',
        'user': 'ZalmanLee',
        'start': '2'
    },
    'another': {
        'lineno': False,
        'start': '-5'
    }
}

TOC = {
    'TOC_HEADERS': '^h[1-6]', # What headers should be included in
                                     # the generated toc
                                     # Expected format is a regular expression

    'TOC_RUN': 'true',    # Default value for toc generation,
                                     # if it does not evaluate
                                     # to 'true' no toc will be generated

    'TOC_INCLUDE_TITLE': 'true',     # If 'true' include title in toc
}