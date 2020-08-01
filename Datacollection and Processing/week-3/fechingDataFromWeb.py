import requests
import json


page =  requests.get('https://api.datamuse.com/words/?rel_rhy=funny')

print(type(page))

response = page.json()

print(type(response))
print(response[0])

print(type(response))

res = json.dumps(response, indent=2)
print(type(res))

query = {'q':'query value', 'q1':'query value'} # Query set in a dictionary

resp = requests.get('ulr',query) # put query in get method
