import requests
from cacheback.decorators import cacheback


@cacheback()
def fetch_tweets(username):
    url = "https://pythonmasterclass.com"
    return requests.get(url % username).json

