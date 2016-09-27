#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Thorin Tabor'
SITEURL = ''
SITENAME = 'Thorin Tabor'
SITETITLE = 'Thorin Tabor'
SITESUBTITLE = 'Software Engineer, Gamer Geek'
SITELOGO = SITEURL + '../images/profile.jpg'
FAVICON = SITEURL + '/images/favicon.ico'

BROWSER_COLOR = '#000000'
ROBOTS = 'index, follow'

COPYRIGHT_YEAR = 2016

PATH = 'content'

THEME = "/Users/tabor/PycharmProjects/tmtabor/Ply"
PLUGIN_PATHS = ['/Users/tabor/PycharmProjects/tmtabor/pelican-plugins']

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

MAIN_MENU = True

MENUITEMS = (('Contact', 'contact.html'),
             ('CV', 'cv.html'),
             ('Games', 'games.html'),
             ('Software', 'software.html'),)
             
DISPLAY_PAGES_ON_MENU = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = 'feeds/%s.rss.xml'

LINKS = ()

# Social widget
SOCIAL = (('github', 'https://github.com/tmtabor'),
          ('linkedin', 'https://www.linkedin.com/in/thorin-tabor-99223627'),
#           ('google', '#'),
#           ('facebook', '#'),
#           ('twitter', '#'),
          ('stack-overflow', 'http://stackoverflow.com/users/4966978/thorin-tabor'),
          ('rss', 'feeds/all.rss.xml'),
#           ('envelope', 'mailto:beholdsa@gmail.com'),
)
          
TWITTER_USERNAME = 'beholdsa'
GITHUB_URL = 'http://github.com/tmtabor'

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Enable i18n plugin.
PLUGINS = ['i18n_subsites']
# Enable Jinja2 i18n extension used to parse translations.
JINJA_EXTENSIONS = ['jinja2.ext.i18n']
