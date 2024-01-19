#!/usr/bin/python3
'''
Module contains a function that makes an api call
'''
import requests


def number_of_subscribers(subreddit):
    '''
    Makes an API call to get the number of
    subscribers in a given subreddit.

    Args:
        subreddit (str): The name of the subreddit
        to check the number of subscribers.

    Returns:
        int: Number of subscribers for the subreddit,
        or 0 if the subreddit is invalid.
    '''
    # URL for the Reddit API endpoint
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # Make a GET request to the API with a custom User-Agent
    data = requests.get(url, headers={'User-agent': 'my-bot'})

    # Check if the request was successful (status code 200)
    if data.status_code == 200:
        # Parse the JSON response to get the number of subscribers
        return data.json().get('data').get('subscribers')
    else:
        # Invalid subreddit or other error, return 0
        print(f"Error: {data.status_code}")
        return 0
