#!/usr/bin/python3
"""get data from reddit API
    """
from requests import get


def top_ten(subreddit):
    """get hot title of a subreddit

    Args:
        subreddit (string): subreddit to check
    """
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json"
    response = get(url, allow_redirects=False, headers={'User-Agent': "myKey"}, params={'limit': 10})
    if response.status_code == 404:
        print(None)
        return

    for res in response.json().get("data").get('children'):
        print(res.get("data").get("title"))

