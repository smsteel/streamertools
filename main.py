import json
from TwitchAPI.Authorization import Authorization


json_data = open("settings.json")
data = json.load(json_data)
auth = Authorization(
    username=data["username"],
    password=data["password"],
    client_id=data["client_id"],
    client_secret=data["client_secret"]
)

