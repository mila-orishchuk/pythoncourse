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
from multiprocessing import Process, Manager
import concurrent
import datetime
from concurrent.futures import ProcessPoolExecutor

manager = Manager()
shared_list = manager.list()


class CommentsDownloader(Process):
    def __init__(self, subreddit):
        super().__init__(target=self.run)
        self._parameters = {'subreddit': subreddit}

    def start(self):
        print('process start')
        super().start()

    def run(self):
        response = requests.get(URL, params=self._parameters)
        if response.ok:
            global shared_list
            shared_list.append(response.json())
        else:
            raise Exception('something went wrong')

    def sort_shared_list(self):
        pass


def create_comments_downloader(subreddit: str):
    process = CommentsDownloader(subreddit)
    process.start()


if __name__ == '__main__':

    FILE = 'comments.json'
    URL = "https://api.pushshift.io/reddit/comment/search/"
    subreddits = ['politics', 'teenagers']
    all_comments = []
    with ProcessPoolExecutor() as executor:
        executor.map(create_comments_downloader, subreddits, timeout=60)
        executor.shutdown()
        for subreddit_comments in shared_list:
            for comment in subreddit_comments['data']:
                all_comments.append(comment)
        all_comments.sort(key=lambda comment: comment['created_utc'])
        
        with open(FILE, 'w') as f:
            f.write(json.dumps(all_comments))
