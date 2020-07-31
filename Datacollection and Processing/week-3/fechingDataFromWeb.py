import requests
import json


page =  requests.get('https://api.datamuse.com/words/?rel_rhy=funny')

print(page)
