import requests

def number_of_subscribers(subreddit, user_agent):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': user_agent}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad responses (4xx and 5xx)
        
        # Parse the JSON response and extract the number of subscribers
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")
    
    # Return 0 for any error
    return 0

# Example usage
if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print("Usage: python3 0-main.py <subreddit> <user_agent>")
    else:
        subreddit = sys.argv[1]
        user_agent = sys.argv[2]
        
        subscribers = number_of_subscribers(subreddit, user_agent)
        
        if subscribers != 0:
            print(f"The subreddit '{subreddit}' has {subscribers} subscribers.")
        else:
            print(f"Failed to retrieve subscriber count for subreddit '{subreddit}'.")
