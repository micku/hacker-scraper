#!/usr/bin/env python

import click


@click.command()
@click.option('--posts',
    default=10,
    help='Number of posts to scrape.',
    type=click.IntRange(
        min=0,
        max=100))
def hacker_scraper(posts):
    """This is a simple CLI applications that scrapes data from Hacker News."""
    click.echo('Number of posts: {}'.format(posts))


if __name__ == '__main__':
    hacker_scraper()
