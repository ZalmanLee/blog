#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'ZalmanLee'
SITENAME = u"zalman's blog"
SITEURL = 'https://blog.0x7c00.me'

PATH = 'content'

STATIC_PATHS = [
    'photo',
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

PLUGIN_PATHS = ['pelican-plugins']

PLUGINS = [
    'gzip_cache',
    'neighbors',
    'sitemap',
    'always_modified',
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