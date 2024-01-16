#!/usr/bin/python3
"""function that queries the Reddit API and returns the no. of subscribers"""

import requests
from sys import argv


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    user = {'User-Agent': 'Kay'}
    url = requests.get('https://www.reddit.com/r/{}/about.json'
                       .format(subreddit), headers=user).json()
    try:
        return url.get('data').get('subscribers')
    except Exception:
        return 0


if __name__ == "__main__":
    number_of_subscribers(argv[1])
