#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """Queries the Reddit API to get the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid or an error occurs.
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "your_unique_user_agent"}  # Replace with your actual User-Agent

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise an exception for non-200 status codes

        data = response.json()
        return data.get("data", {}).get("subscribers", 0)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching subreddit data: {e}")
        return 0

