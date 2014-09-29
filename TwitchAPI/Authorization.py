from TwitchAPI.Request import Request
from TwitchAPI.Scopes import Scopes


class Authorization:

    grant_type = "password"
    request = "/oauth2/token"
    version = 3
    access_token = ""

    def __init__(self, username, password, client_id, client_secret):
        scope = Scopes(user_read=True)
        payload = {
            'grant_type': self.grant_type,
            'client_id': client_id,
            'client_secret': client_secret,
            'scope': scope,
            'username': username,
            'password': password,
        }
        r = Request(self.version, self.request, payload)
        print(r.post())