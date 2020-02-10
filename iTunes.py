import requests

BASEURL = "https://itunes.apple.com/search"
params = ##########
response = requests.get(BASEURL, params)
stat = response.status_code
