import requests as requests
r = requests.get('http://httpbin.org/get')
p = requests.post('http://httpbin.org/post')
pt = requests.put('http://httpbin.org/put')
d = requests.delete('http://httpbin.org/delete')

r = requests.get('http://httpbin.org/get')
r.text

r = requests.get('http://httpbin.org/get')
r.status_code
200

r = requests.get('http://httpbin.org/get')
r.elapsed
0.56127340

import requests
import json
url = "https://api.covid19api.com/summary"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

result = json.loads(response.text)


print(result)

import requests
import json
url = "https://api.covid19api.com/summary"
payload = {}
headers= {}
response = requests.request("GET", url, headers=headers, data = payload)
result = json.loads(response.text)
print(result["Global"])

import requests
import json
url = "https://api.covid19api.com/total/country/Turkey/status/confirmed"
payload = {}
headers= {}
response = requests.request("GET", url, headers=headers, data = payload)
result = json.loads(response.text)
print(result)