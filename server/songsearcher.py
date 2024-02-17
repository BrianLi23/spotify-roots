import base64
import os
from auth_code_flow import FlowManager
from dotenv import load_dotenv
from requests import post, get
import json
from lyricsgenius import Genius

# Load key
load_dotenv(".env")

class SongSearcher:

    def __init__(self, searchInput, searchType):
        self.searchInput = searchInput
        self.searchType = searchType
        self.private_client_id = os.getenv("CLIENT_ID")
        self.private_client_secret = os.getenv("CLIENT_SECRET_ID")
        self.genius_token = os.getenv("GENIUS_ACCESS_TOKEN")
        self.token = self.get_token()
        self.result = self.search_query(searchInput, searchType, self.token)
        self.genius = Genius(self.genius_token, sleep_time=0.01, verbose=False, remove_section_headers=True, skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"])
    
    # Get access token
    def get_token(self):
        auth_string = f"{self.private_client_id}:{self.private_client_secret}"
        auth_bytes = auth_string.encode("utf-8")
        auth_base64 = str(base64.b64encode(auth_bytes).decode("utf-8"))

        url = "https://accounts.spotify.com/api/token"
        headers = {
            "Authorization": "Basic " + auth_base64,
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {"grant_type": "client_credentials"}
        result = post(url, headers=headers, data=data)

        # loads (load from string) covert json to python dictionary
        json_result = json.loads(result.content)

        # access_token is the key in the dictionary, parse token
        token = json_result["access_token"]
        return token

    # Get authorization header
    def get_auth_header(self, token):
        return {"Authorization": "Bearer " + token}

    def search_query(self, name, search_type, token):
        url = "https://api.spotify.com/v1/search"
        headers = self.get_auth_header(token)
        query = f"?q={name}&type={search_type}&limit=1"

        query_url = url + query
        result = get(query_url, headers=headers)
        json_result = json.loads(result.content)

        if len(json_result) == 0:
                print("No artist with this name exists")
                return None
        
        return json_result
    # Get song lyrics
    def get_lyrics(self, song_name, artist_name):
        song = self.genius.search_song(song_name, artist_name)
        if song == None:
            print("Can't find the song name")
            return None
        else:
            return song.lyrics

    
if __name__ == "__main__":
    searcher = SongSearcher("ikon love scenario", "track")
    if searcher.searchType == "album":
        artist_name = searcher.result["albums"]["items"][0]["artists"][0]["name"]
        album_name = searcher.result["albums"]["items"][0]["name"]
        album_release = searcher.result["albums"]["items"][0]["release_date"]
        picture_url = ["albums"]["items"][0]["images"][0]["url"]
        print(artist_name, album_name, album_release, picture_url)  
    elif searcher.searchType == "artist":
        artist_name = searcher.result["artists"]["items"][0]["name"]
        picture_url = searcher.result["artists"]["items"][0]["images"][0]["url"]
        print(artist_name, picture_url)
    elif searcher.searchType == "track":
        song_name = searcher.result["tracks"]["items"][0]["name"]
        album_name = searcher.result["tracks"]["items"][0]["album"]["name"]
        artist_name = searcher.result["tracks"]["items"][0]["artists"][0]["name"]
        picture_url = searcher.result["tracks"]["items"][0]["album"]["images"][0]["url"]
        print(song_name, album_name, artist_name, picture_url)