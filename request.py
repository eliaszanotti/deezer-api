import http.client
import json

def deezer(request_str) :
    http_client = http.client.HTTPSConnection("api.deezer.com")
    http_client.request("GET", request_str)
    result = http_client.getresponse()
    data = result.read()
    json_dictionary = json.loads(data.decode("utf-8"))
    return json_dictionary

def lyric(request_str) : 
    http_client = http.client.HTTPSConnection("api.musixmatch.com/ws/1.1")
    http_client.request("GET", request_str)
    result = http_client.getresponse()
    print(result)
    data = result.read()
    json_dictionary = json.loads(data.decode("utf-8"))
    return json_dictionary

# print(lyric("/track.search?q_track=poizon&apikey=badb0f5f69cf84c065ec36cd795e495e"))
# print(lyric(""))
# lyric_request("/track.search='elias'")