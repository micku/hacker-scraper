# Hacker Scraper
This is a simple CLI applications that scrapes data from [Hacker News](https://news.ycombinator.com/).

## Installation
The application can run under [Docker](https://www.docker.com/), here are the instructions to get it to work.

1. [Install Docker](https://docs.docker.com/engine/installation/#installation)
2. Pull the Python image: `docker pull python`
3. Run it: `docker run -it --rm --name my-running-script -v "$PWD":/usr/src/app -w /usr/src/app python:2 python hacker_scraper.py`
