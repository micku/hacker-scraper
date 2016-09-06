# Hacker Scraper
This is a simple CLI applications that scrapes data from [Hacker News](https://news.ycombinator.com/).

## Installation
The application can run under [Docker](https://www.docker.com/), here are the instructions to get it to work.

1. [Install Docker](https://docs.docker.com/engine/installation/#installation)
2. Pull the Python image `docker pull python`
3. Build the container: `docker build -t hacker_scraper .`
4. Run it: `docker run -it --rm --name hacker-scraper hacker_scraper`

## External dependencies
* [Click](http://click.pocoo.org/6/): CLI dedicated package that is really useful to keep code clean and don't reinvent the wheel
