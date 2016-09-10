#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import click
import requests
import re
import json
from rfc3986 import uri_reference


SITE_URL = 'https://news.ycombinator.com/'
NEXT_PAGE_CLASS = 'morelink'
ARTICLE_CLASS = 'athing'


@click.command()
@click.option('--posts', default=10,
    help='Number of posts to scrape.',
    type=click.IntRange(min=0, max=100))
def hacker_scraper(posts):
    """This is a simple CLI applications that scrapes data from Hacker News.

    :param posts: The number of posts to scrape
    :type posts: int
    """
    all_articles = []

    for idx, article in enumerate(get_all_articles()):
        if idx >= posts:
            break
        all_articles.append(article)

    click.echo(json.dumps(all_articles))


def get_all_articles(url = None):
    """ Loops through all posts of HN, changing page when reaches the end, and
    yields the results.

    :param url: URL of the page to scrape, if None the default is the
    value of SITE_URL
    :type url: str
    """
    page = requests.get(url or SITE_URL)

    source = BeautifulSoup(page.content, 'html.parser')

    next_page_path = source.find(class_ = NEXT_PAGE_CLASS)['href']
    next_page_url = '{}{}'.format(SITE_URL, next_page_path)

    articles = source.find_all(class_ = ARTICLE_CLASS)
    for article in [
            parse_article(x)
            for x
            in articles
            ]:
        if is_valid(article):
            yield article

    for article in get_all_articles(next_page_url):
        yield article


def is_valid(article):
    strings = {
        'title',
        'author',
        'uri',
    }

    # Checks if the property is a string or unicode
    is_string = [
        isinstance(article[x], str) \
            or isinstance(article[x], unicode)
        for x
        in strings
    ]
    if not all(is_string):
        return False

    # Checks if the string is longest than 0 and shortest than 257 chars
    is_short = [
        len(article[x]) > 0 \
            and len(article[x]) < 257
        for x
        in strings
    ]
    if not all(is_short):
        return False

    ints = {
        'points',
        'comments',
        'rank',
    }

    is_int = [
        isinstance(article[x], int) \
            and article[x] >= 0
        for x
        in ints
    ]
    if not all(is_int):
        return False

    uri = uri_reference(article['uri'])
    if not uri.is_valid():
        return False

    return True


def parse_article(article):
    """Parses the article from HTML to Python object.

    :param article: Input HTML to be parsed
    :type article: str
    """
    other_info = article.next_sibling
    return {
        'title': article.find(class_ = 'storylink').text,
        'uri': article.find(class_ = 'storylink')['href'],
        'author': other_info.find_all(class_ = 'hnuser')[0].text \
            if len(other_info.find_all(class_ = 'hnuser')) > 0
            else None,
        'points': only_numbers(other_info.find(class_ = 'score').text) \
            if other_info.find(class_ = 'score') is not None \
            else None,
        'comments': only_numbers(other_info.find_all('a')[-1].text) \
            if other_info.find_all('a')[-1] is not None \
            else None,
        'rank': only_numbers(article.find(class_ = 'rank').text) \
            if article.find(class_ = 'rank') is not None \
            else None,
    }


def only_numbers(text):
    """Strips all non-digits characters from the input string

    :param text: Input string to be stripped
    :type text: str
    """
    stripped = re.sub(u'[^0-9]*', '', text)
    return int(stripped) if len(stripped) > 0 else 0


if __name__ == '__main__':
    hacker_scraper()
