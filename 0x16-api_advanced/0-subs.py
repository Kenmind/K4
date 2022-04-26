#!/usr/bin/python3
""" Returns the number of subscribers or a given subreddit """
import requests as r


def number_of_subscribers(subreddit):
    """ Returns the number of subscribers for a given subreddit
        Returns 0 if a given subreddit is invalid """
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    head = {"User-Agent": "Holberton"}
    req = r.get(url, headers=head)
    if req.status_code == 200:
        return req.json().get("data", None).get("subscribers", None)
    else:
        return 0
