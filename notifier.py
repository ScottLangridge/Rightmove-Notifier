import logging

import requests


class Notifier:
    def __init__(self, user_key, api_key):
        self.user_key = user_key
        self.api_key = api_key

    def send_msg(self, title, message):
        url = 'https://api.pushover.net/1/messages.json'
        post_data = {'user': self.user_key, 'token': self.api_key, 'title': title, 'message': message}
        response = requests.post(url, data=post_data)
        # logging.info(f'Sent notification - status code: {response.status_code} - response: {response.text}')
