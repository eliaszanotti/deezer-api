import request

def search_album(search_query) : 
    request_str = '/search?q=album:"' + search_query + '"'
    search = request.deezer(request_str)
    return search["data"]

def get_cover(id_album) : 
    request_str = '/album/' + str(id_album)
    album = request.deezer(request_str)
    return album["cover_xl"]

def search_results(search_query) : 
    new_query = ""
    for char in search_query : 
        if char == " " or char == '"' or char == "'" :
            new_query += "_"
        else : 
            new_query += char 
    result = search_album(new_query)
    list_albums = []
    for i in range(len(result)) : 
        artist = result[i]["artist"]["name"]
        album = result[i]["album"]["title"]
        cover_link = get_cover(result[i]["album"]["id"])
        final = str(artist) + " - " + str(album) + " | " + str(cover_link)
        if final not in list_albums : 
            list_albums.append(final)
    for album in list_albums : 
        print(album)
    return 

if __name__ == "__main__" : 
    search_results('feu')