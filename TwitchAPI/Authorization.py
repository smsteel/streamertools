from TwitchAPI.Request import Request
from TwitchAPI.Scopes import Scopes


class Authorization(Request):

    grant_type = "password"
    request = "/oauth2/token"
    version = 3
    access_token = None

    def get_access_token(self, username, password, client_id, client_secret):
        scope = Scopes(user_read=True)
        payload = {
            'grant_type': self.grant_type,
            'client_id': client_id,
            'client_secret': client_secret,
            'scope': scope,
            'username': username,
            'password': password,
        }
        token = self.post(payload)
        print(token)