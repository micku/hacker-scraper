# -*- coding: utf-8 -*-

#!/usr/bin/env python

from bs4 import BeautifulSoup
import click
import requests
import re
import json


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
    for article in articles:
        yield parse_article(article)

    for article in get_all_articles(next_page_url):
        yield article


def parse_article(article):
    """Parses the article from HTML to Python object.

    :param article: Input HTML to be parsed
    :type article: str
    """
    other_info = article.next_sibling
    return {
        'title': article.find_all(class_ = 'storylink')[0].text,
        'uri': article.find_all(class_ = 'storylink')[0]['href'],
        'author': other_info.find_all(class_ = 'hnuser')[0].text,
        'points': only_numbers(other_info.find(class_ = 'score').text),
        'comments': only_numbers(other_info.find_all('a')[-1].text),
        'rank': only_numbers(article.find(class_ = 'rank').text),
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
