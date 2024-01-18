#!/usr/bin/python3
"""Quering Reddit"""

import requests


def number_of_subscribers(subreddit):
    """query a subreddit and retrieve the number of subscribers"""

    # Reddit API endpoint for getting subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent to avoid too many requests error
    headers = {'User-Agent': 'My user Agent 1.0'}

    # send a GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful and not redirect
    if response.status_code == 200 and not response.is_redirect:
        # parse JSON response to extract the number of subscribers
        data = response.json().get('data', {})
        sub_count = data.get('subscribers', 0)
        return sub_count
    else:
        return 0
