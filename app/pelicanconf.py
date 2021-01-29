#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Brian Grohe'
SITENAME = 'Brian Grohe'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Home', '/'),
         ('Blog', '/blog.html'),)

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/bgrohe/'),
          ('github', 'https://github.com/paxnovem'),
          ('twitter', 'https://twitter.com/grohe43'),
          ('envelope', 'mailto:brian@briangrohe.com'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "/code/Flex"

INDEX_SAVE_AS = 'blog.html'
DISPLAY_PAGES_ON_MENU = False
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# theme settings
SITELOGO = SITEURL + "/images/profile.jpg"