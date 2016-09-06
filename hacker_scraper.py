#!/usr/bin/env python

import click


@click.command()
@click.option('--posts', default=10, help='Number of posts to scrape.')
def hacker_scraper(posts):
    click.echo('Number of posts: {}'.format(posts))


if __name__ == '__main__':
    hacker_scraper()
