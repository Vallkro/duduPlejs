import requests
import json
key = '0D5B504EC602C60622BF68C9951F527C'
#response = requests.get("https://api.open-notify.org/astros.json")
API = 'https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?format=XML&key=' + key
#response = requests.get(API)
#print(response.status_code)
#
#match_id = '6442066317'
#API = f'https://api.opendota.com/api/matches/{match_id}'
#response = requests.get(API)
#print(response.status_code)

steamID = '76561198005640593'

API = f'https://api.opendota.com/api/players/{steamID}'
#API = f'https://api.opendota.com/api/players/{steamID}/recentMatches'
response = requests.get(API)
print(response.status_code)

x = json.loads(response.json())

with open('temp.json', 'w') as outfile:
    json.dump(x, outfile)