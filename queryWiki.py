#!/usr/bin/python3
"""

	get_category_items.py
	

    MediaWiki Action API Code Samples
    Demo of `Categorymembers` module : List twenty items in a category.
    MIT license
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    'action': "query",
    'list': "categorymembers",
    'cmtitle': "Category:Physics",
    'cmlimit': 20,
    'cmtype': "page",
    'format': "json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)