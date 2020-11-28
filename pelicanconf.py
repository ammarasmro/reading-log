#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Ammar Asmro'
SITENAME = 'ReadingLog'
SITEURL = 'https://ammarasmaro.com/reading-log'

PATH = 'content'

TIMEZONE = 'America/Toronto'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('AmmarAsmaro.com', 'https://ammarasmaro.com/'),)
        #  ('Python.org', 'https://www.python.org/'),
        #  ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
        #  ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('ammar-asmro ', 'https://www.linkedin.com/in/ammar-asmro/'),
          ('ammarasmro', 'https://twitter.com/ammarasmaro'),)

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# THEME = "/Users/ammarasmro/.pyenv/versions/3.8.5/envs/reading_pelican_env/lib/python3.8/site-packages/pelican/themes/simple"
THEME = "notmyidea"
