# Hacker Scraper
This is a simple CLI applications that scrapes data from [Hacker News](https://news.ycombinator.com/).

### Output format

```json
[
    {
        "title": "Web Scraping in 2016",
        "uri": "https://franciskim.co/2016/08/24/dont-need-no-stinking-api-web-scraping-2016-beyond/",
        "author": "franciskim",
        "points": 133,
        "comments": 80,
        "rank": 1
    },
    {
        "title": "Instapaper is joining Pinterest",
        "uri": "http://blog.instapaper.com/post/149374303661",
        "author": "ropiku",
        "points": 182,
        "comments": 99,
        "rank": 2
    }
]
```

### Input arguments
The application takes only one optional value:

- `--posts` how many posts to print. A positive integer <= 100.

Default value for `--posts` is `10`.

```
hacker_scraper --posts n
```



## Installation
The application can run under [Docker](https://www.docker.com/), here are the instructions to get it to work.

1. [Install Docker](https://docs.docker.com/engine/installation/#installation)
2. Pull the Python image `docker pull python`
3. Build the container: `docker build -t hacker_scraper .`
4. Run it: `docker run -t --rm hacker_scraper python hacker_scraper.py --posts 20`

## External dependencies
* [Click](http://click.pocoo.org/6/): CLI dedicated package that is really useful to keep code clean and don't reinvent the wheel
