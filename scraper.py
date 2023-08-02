import logging
import time
from requests.exceptions import ConnectionError
from secrets import Secrets

import requests

from notifier import Notifier


class Scraper:
    def __init__(self, target_urls):
        self.targets = target_urls

    def fetch_pages(self):
        raw_results = []
        for i in self.targets:
            print('Fetching ' + i)
            try:
                response = requests.get(i)
            except ConnectionError as e:
                logging.error(e)
                continue

            if response.status_code != 200:
                Notifier(Secrets.PUSHOVER_USER_KEY, Secrets.PUSHOVER_API_KEY).send_msg('ERROR', response.text)
            else:
                raw_results.append(response.text)
        return raw_results
