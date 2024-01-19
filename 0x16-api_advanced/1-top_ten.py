#!/usr/bin/python3
"""Func to print hot posts on a given Reddit subreddit."""
import requests

def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a subreddit."""
    # Construct the URL for the subreddit's hot posts in JSON format
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    
    # Define the user-agent header
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    
    # Set parameters for the request, limiting the response to 10 posts
    params = {
        "limit": 10
    }
    
    # Send the HTTP GET request to the Reddit API
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    # Check if the subreddit exists (status code 404), and handle accordingly
    if response.status_code == 404:
        print("None")
        return
    
    # Extract the JSON data from the response
    results = response.json().get("data")
    
    # Print the titles of the 10 hottest posts
    [print(c.get("data").get("title")) for c in results.get("children")]

# Example usage:
# Replace 'example_subreddit' with the desired subreddit name
top_ten('example_subreddit')
