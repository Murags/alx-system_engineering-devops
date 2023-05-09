#!/usr/bin/python3
"""get data from reddit API
    """
from requests import get


def count_words(subreddit, word_list, params={}, hot_list=[], counter=0):
    """get hot title of a subreddit

    Args:
        subreddit (string): subreddit to check
    """
    print(counter)

    if (params.get('after') is None and counter != 0):
        for word in word_list:
            appearance = 0
            for title in hot_list:
                appearance += title.upper().count(word.upper())
            if appearance != 0:
                print("{}: {}".format(word, appearance))
        return

    url = "https://www.reddit.com/r/" + subreddit + "/hot.json"
    response = get(url, allow_redirects=False,
                   headers={'User-Agent': "myKey"}, params=params)
    if response.status_code == 404:
        return
    params['after'] = response.json().get('data').get('after')
    params['before'] = response.json().get('data').get('before')

    for res in response.json().get("data").get('children'):
        hot_list.append(res.get("data").get("title"))
    counter += 1
    return count_words(subreddit, word_list, params, hot_list, counter)
