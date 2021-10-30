import http.client
import json

def deezer_request(request_str) :
    http_client = http.client.HTTPSConnection("api.deezer.com")
    http_client.request("GET", request_str, )
    result = http_client.getresponse()
    data = result.read()
    json_dictionary = json.loads(data.decode("utf-8"))
    return json_dictionary

def search(search_query) : 
    request_str = '/search?q=album:"' + search_query + '"'
    search = deezer_request(request_str)
    return search["data"]

def search_results(search_query) : 
    result = search(search_query)
    for i in range(len(result)) : 
        artist = result[i]["artist"]["name"]
        album = result[i]["album"]["title"]
        print(artist, "-", album)

print(search_results("feu"))



