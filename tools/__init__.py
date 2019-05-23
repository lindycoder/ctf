import re

import requests
from bs4 import BeautifulSoup


def open_html(url, **kwargs):
    print(f"Opening : {url}")
    response = requests.get(url, **kwargs)

    if response.status_code < 200 or response.status_code >= 300:
        raise Exception(f"Problem? {response.status_code} : {response.content}")

    return BeautifulSoup(response.content.decode(), features='html.parser')


def first(iterable):
    return next(iter(iterable))


def parse_one(pattern, content):
    matches = re.match(pattern, content, flags=re.DOTALL)

    if matches:
        return matches.group(1)

    raise Exception(f"Did not match: {pattern}, {content}")