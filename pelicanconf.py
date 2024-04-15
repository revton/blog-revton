AUTHOR = 'Revton Braga'
SITENAME = 'Revton Braga'
SITEURL = "https://revton.github.io/blog-revton"

PATH = "content"

TIMEZONE = 'Europe/Lisbon'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    # ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    # ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    # ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("Github", "https://github.com/revton"),
    ("Linkedin", "https://www.linkedin.com/in/revton"),
    ("X", "https://x.com/revton"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
STATIC_PATHS = ["extra"]

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}, 
}