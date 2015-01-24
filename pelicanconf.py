#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Joao Mauricio Rosal'
SITENAME = u'Componente Principal'
SITEURL = ''

PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['economia', 'cultura', 'misc', 'tecnico']
FILENAME_METADATA = '(?P<slug>.*)'
PAGE_URLS = ('{slug}.html')


# DATE_FORMATS = {'pt': ('pt_BR', '%d/%m/%Y')}
TIMEZONE = 'America/Sao_Paulo'
DEFAULT_LANG = u'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Themes
THEME = "gum"
STATIC_PATHS = ['./static/images']
HEADER_IMAGE = 'free-header-image-1.jpg'

# Menu Items
# MENUITEMS = [('Tech', './tech.html'),
#              ('About me', './about.html'),
#              ('Contacts', './contacts.html')]
DISPLAY_PAGES_ON_MENU = True


# Blogroll
USE_FOLDER_AS_CATEGORY = True
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Openculture', 'http://www.openculture.com'),
         ('Coursera', 'http://www.coursera.org'))

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 4


# Development
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False
LOAD_CONTENT_CACHE = False

