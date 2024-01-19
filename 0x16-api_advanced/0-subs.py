#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers for a given subreddit."""

    headers = {'User-Agent': 'your_user_agent_here'}  # Replace with your actual user agent
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            data = response.json()
            return data['data']['subscribers']
        except (KeyError, ValueError):  # Handle cases where expected keys are missing
            return 0
    else:
        return 0
