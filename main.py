import http.client
import json

http_client = http.client.HTTPSConnection("api.deezer.com")
http_client.request("GET", "/track/3135556", )
result = http_client.getresponse()
data = result.read()
json_dictionary = json.loads(data.decode("utf-8"))

print(json_dictionary["title"])

# print(data.decode("utf-8"))




# Load API response into a Python dictionary object, encoded as utf-8 string
