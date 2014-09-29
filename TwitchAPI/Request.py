import requests


class Request:

    __mime_type = "application/vnd.twitchtv.v{version}+json"
    url = "https://api.twitch.tv/kraken"

    def __init__(self, version, request, payload):
        self.payload = payload
        self.headers = {
            'Accept': self.__mime_type.format(version=version)
        }
        print(self.headers)
        self.request = request

    def get(self):
        r = requests.get(self.url + self.request, headers=self.headers, params=self.payload)
        return r.json()

    def post(self):
        r = requests.post(self.url + self.request, headers=self.headers, params=self.payload)
        print(r.url)
        return r.json()