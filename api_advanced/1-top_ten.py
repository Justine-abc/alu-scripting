#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit"""

import requests

def top_ten(subreddit):
    """Queries the Reddit API and prints titles of the first 10 hot posts"""
    URL = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    HEADERS = {"User-Agent": "CustomUserAgent/1.0"}

    try:
        response = requests.get(URL, headers=HEADERS, allow_redirects=False)
        
        # Check if the request was successful
        if response.status_code != 200:
            print("None")
            return
        
        # Parse JSON response and print titles
        data = response.json().get("data", {}).get("children", [])
        if not data:
            print("None")
        else:
            for post in data:
                print(post.get("data", {}).get("title"))

    except Exception:
        print("None")

