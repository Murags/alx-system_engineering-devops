#!/usr/bin/python3
"""gets data from reddit API
    """
from requests import get


def number_of_subscribers(subreddit):
    """gets subscibers of a subbredit

    Args:
        subreddit (string): subreddit to check
    """
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    response = get(url, headers={'User-Agent': "myKey"}, allow_redirects=False)
    if response.status_code == 404:
        return (0)
    res = response.json().get("data").get("subscribers")

    return (res)
