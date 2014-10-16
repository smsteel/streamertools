import requests


class Request:

    __mime_type = "application/vnd.twitchtv.v{version}+json"
    url = "https://api.twitch.tv/kraken"
    version = 2
    request = ""

    def __get_headers(self):
        return {
            'Accept': self.__mime_type.format(version=self.version)
        }

    def get(self, payload):
        r = requests.get(self.url + self.request, headers=self.__get_headers(), params=payload)
        return r.json()

    def post(self, payload):
        r = requests.post(self.url + self.request, headers=self.__get_headers(), params=payload)
        print(r.url)
        return r.json()