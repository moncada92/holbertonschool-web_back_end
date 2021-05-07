#!/usr/bin/python3
""" count it!
"""

import requests


def count_words(subreddit, word_list):
    """ prints a sorted count of given keywords
    """
    headers = {"User-Agent": ""}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    data = requests.get(url, headers=headers, allow_redirects=False).json()
    print(data)