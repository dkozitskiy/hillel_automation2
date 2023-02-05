import json
import requests


class BaseAPI:
    def __init__(self):
        self.__request = requests

    def get(self, base_url, url):
        response = self.__request.get(f'{base_url}{url}')
        return response

    def post(self, base_url, url, body=None):
        response = self.__request.post(f'{base_url}{url}', json=body)
        return response

    def put(self, base_url, url, body=None):
        response = self.__request.post(f'{base_url}{url}', json=body)
        return response

    def delete(self, base_url, url, body=None):
        response = self.__request.post(f'{base_url}{url}', json=body)
        return response
