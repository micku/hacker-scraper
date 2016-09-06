#!/usr/bin/env python

import click


@click.command()
def hacker_scraper():
    click.echo('Here comes click')


if __name__ == '__main__':
    hacker_scraper()
