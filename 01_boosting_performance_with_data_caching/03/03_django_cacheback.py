import requests
from cacheback.decorators import cacheback


@cacheback()
def fetch_tweets(username):
    url = "https://twitter.com/statuses/user_timeline.json?screen_name=%s"
    return requests.get(url % username).json
