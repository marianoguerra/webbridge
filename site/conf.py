# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import time

##############################################
# Configuration, please edit
##############################################


# Data about this site
BLOG_AUTHOR = "Mariano Guerra"
BLOG_TITLE = "Web Bridge Stuttgart"
# This is the main URL for your site. It will be used
# in a prominent link
SITE_URL = "https://marianoguerra.github.io/webbridge/"
# This is the URL where nikola's output will be deployed.
# If not set, defaults to SITE_URL
# BASE_URL = "http://nikola.ralsina.com.ar"
BLOG_EMAIL = "luismarianoguerra+webbride@gmail.com"
BLOG_DESCRIPTION = "Web Technology Learning Community in Stuttgart"

# What is the default language?
DEFAULT_LANG = "en"

# What other languages do you have?
# The format is {"translationcode" : "path/to/translation" }
# the path will be used as a prefix for the generated pages location
TRANSLATIONS = {
    "en": "",
    "de": "./de"
}

# What will translated input files be named like?

# If you have a page something.rst, then something.pl.rst will be considered
# its Polish translation.
#     (in the above example: path == "something", ext == "rst", lang == "pl")
# this pattern is also used for metadata:
#     something.meta -> something.pl.meta
TRANSLATIONS_PATTERN = "{path}.{ext}.{lang}"

# Links for the sidebar / navigation bar.
# You should provide a key-value pair for each used language.
NAVIGATION_LINKS = {
    "en": (
        ('/', 'Start'),
        ('/news/', 'News'),
        ('/schedule/', 'Schedule'),
        ('/location/', 'Location'),
        ('/sponsors/', 'Sponsors'),
        ('/contact/', 'Contact'),
    ),
    "de": (
        ('/de/', 'Startseite'),
        ('/de/news/', 'Nachricten'),
        ('/de/schedule/', 'Programm'),
        ('/de/location/', 'Platz'),
        ('/de/sponsors/', 'Sponsoren'),
        ('/de/contact/', 'Kontakt'),
    ),
}


POSTS = (
    ("posts/*.txt", "news", "post.tmpl"),
    ("posts/*.rst", "news", "post.tmpl"),
)
PAGES = (
    ("stories/*.txt", "", "story.tmpl"),
    ("stories/*.rst", "", "story.tmpl"),
)

COMPILERS = {
    "rest": ('.txt', '.rst'),
    "markdown": ('.md', '.mdown', '.markdown'),
    "textile": ('.textile',),
    "txt2tags": ('.t2t',),
    "bbcode": ('.bb',),
    "wiki": ('.wiki',),
    "ipynb": ('.ipynb',),
    "html": ('.html', '.htm')
}

INDEX_PATH = "news"

THEME = 'bootstrap3'

CONTENT_FOOTER = 'Contents &copy; {date}         <a href="mailto:{email}">{author}</a> - Powered by         <a href="https://getnikola.com">Nikola</a>'
CONTENT_FOOTER = CONTENT_FOOTER.format(email=BLOG_EMAIL,
                                       author=BLOG_AUTHOR,
                                       date=time.gmtime().tm_year)

PRETTY_URLS = True
SHOW_SOURCELINK = False
WRITE_TAG_CLOUD = False

GLOBAL_CONTEXT = {}

# For more information on options that you can use in this file, see
# https://getnikola.com/conf.html

COMMENT_SYSTEM = ""
