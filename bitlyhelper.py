from urllib.request import urlopen
import json


TOKEN = "e4a2fbd6f8d1b8b6241066a02f1bec4ecf1d8612"
ROOT_URL = "https://api-ssl.bitly.com"
SHORTEN = "/v3/shorten?access_token={}&longUrl={}"

class BitlyHelper:
    def shorten_url(self, longurl):
        try:
            url = ROOT_URL + SHORTEN.format(TOKEN, longurl)
            response = urlopen(url).read().decode('utf-8')
            jr = json.loads(response)
            return jr['data']['url']
        except Exception as e:
            print(e)
