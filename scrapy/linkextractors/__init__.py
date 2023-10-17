"""
scrapy.linkextractors

This package contains a collection of Link Extractors.

For more info see docs/topics/link-extractors.rst
"""
import re

# common file extensions that are not followed if they occur in links
IGNORED_EXTENSIONS = []


_re_type = type(re.compile("", 0))


def _matches(url, regexs):
    return any(r.search(url) for r in regexs)


def _is_valid_url(url):
    return url.split("://", 1)[0] in {"http", "https", "file", "ftp"}


# Top-level imports
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor as LinkExtractor
