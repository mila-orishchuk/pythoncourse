"""
Requests using concurrent and multiprocessing libraries
Download all comments from a subreddit of your choice using
URL: https://api.pushshift.io/reddit/comment/search/ . 

As a result, store all comments in chronological order in JSON
and dump it to a file. For this task use concurrent and multiprocessing
libraries for making requests to Reddit API.
"""


import requests
import json
from multiprocessing import Process
import concurrent
import datetime
import time
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logging.basicConfig(format="[%(asctime)s] [%(levelname)s] {%(filename)s:%(lineno)d} {%(process)d:%(threadName)s} - %(message)s")



class CommentsDownloader(Process):
    def __init__(self, author, parameters):
        super().__init__()
        self._author = author
        self._parameters = parameters

    def run(self):
        response = requests.get(URL, params=self._parameters)
        if response.ok:
            with open(FILE, 'a+') as file:
                json.dump(response.json(), file, indent=4)
                file.write(',\n')
        else:
            raise Exception


if __name__ == '__main__':
    FILE = 'comments.json'
    URL = "https://api.pushshift.io/reddit/comment/search/"
    
    for author in author_list:
        params = {'size': 5, 'author': author, 'fields': ('author', 'body', 'created_utc', 'subreddit')}
        thread = CommentsDownloader(author, params)
        thread.start()
        thread.join()