from flask import Flask, request, redirect, jsonify, session
from requests import post, get
from dotenv import load_dotenv
from flask_cors import CORS
import os
import urllib.parse
import datetime
import songsearcher
import langchainfunc

app = Flask(__name__)
CORS(app)
app.secret_key = "secret"

load_dotenv(".env")

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET_ID")
redirect_uri = os.getenv("REDIRECT_URI")

auth_url = "https://accounts.spotify.com/authorize"
token_url = "https://accounts.spotify.com/api/token"
api_url = "https://api.spotify.com/v1/"

artist_name = ""
album_name = ""
album_release = ""
song_name = ""
picture_url = ""
text_output = ""


@app.route("/api/search", methods=["POST", "GET"])
def searchbar():
    global artist_name, album_name, album_release, song_name, picture_url, text_output

    if request.method == 'POST':
        data = request.json
        print("Received request with data:", data)  # For debugging
        search_query = data.get("search_query", "")
        search_type = data.get("search_type", "track") # default to track if not provided

        searcher = songsearcher.SongSearcher(search_query, search_type)

        if searcher.searchType == "album":
            artist_name = searcher.result["albums"]["items"][0]["artists"][0]["name"]
            album_name = searcher.result["albums"]["items"][0]["name"]
            album_release = searcher.result["albums"]["items"][0]["release_date"]
            picture_url = ["albums"]["items"][0]["images"][0]["url"]
            output = langchainfunc.LangChainFunc("", album_name=album_name, artist_name=artist_name)
            text_output = output.text_output()
            

            return jsonify({
            'artist_name': artist_name,
            'album_name': album_name,
            'album_release': album_release,
            'picture_url': picture_url,
            'output': text_output
            })
            

        elif searcher.searchType == "artist":
            artist_name = searcher.result["artists"]["items"][0]["name"]
            picture_url = searcher.result["artists"]["items"][0]["images"][0]["url"]
            output = langchainfunc.LangChainFunc("", "", artist_name=artist_name)
            text_output = output.text_output()

            return jsonify({
            'artist_name': artist_name,
            'picture_url': picture_url
            })

        elif searcher.searchType == "track":
            song_name = searcher.result["tracks"]["items"][0]["name"]
            album_name = searcher.result["tracks"]["items"][0]["album"]["name"]
            artist_name = searcher.result["tracks"]["items"][0]["artists"][0]["name"]
            picture_url = searcher.result["tracks"]["items"][0]["album"]["images"][0]["url"]
            print(artist_name, album_name, song_name, picture_url)
            output = langchainfunc.LangChainFunc(song_name=song_name, album_name=album_name, artist_name=artist_name)
            text_output = str(output.text_output())
            print(text_output)

            return jsonify({
            'artist_name': artist_name,
            'album_name': album_name,
            'song_name': song_name,
            'picture_url': picture_url,
            'output': text_output
            })
    else:
        return jsonify({
            'artist_name': artist_name,
            'album_name': album_name,
            'song_name': song_name,
            'picture_url': picture_url,
            'output': text_output
            })


# @app.route("/login")
# def login():
#     scopes = "user-read-private user-read-email"

#     params = {
#         "client_id": client_id,
#         "response_type": "code",
#         "redirect_uri": redirect_uri,
#         "scope": scopes,
#     }
    
#     full_auth_url = f"{auth_url}?{urllib.parse.urlencode(params)}"

#     return redirect(full_auth_url)

# @app.route("/callback")
# def callback():
#     if 'error' in request.args:
#         return jsonify({"Error: " + request.args['error']})
    
#     if 'code' in request.args:
        
#         req_body = {
#             "grant_type": "authorization_code",
#             "code": request.args['code'],
#             "redirect_uri": redirect_uri,
#             "client_id": client_id,
#             "client_secret": client_secret,
#         }

#         response = post(token_url, data=req_body)
#         token_info = response.json()

#         session['access_token'] = token_info['access_token']
#         session['refresh_token'] = token_info['refresh_token']
#         session['expires_at']  = datetime.datetime.now().timestamp() 
#         + token_info['expires_in']

#         return redirect('/playlists')
    
# @app.route("/playlists")
# def get_playlists():
#     if 'access_token' in session:
#         if datetime.datetime.now().timestamp() > session['expires_at']:
#             return redirect('/refresh-token')
        
#     else:
#         return redirect('/login')
    
#     headers = {"Authorization": "Bearer " + session['access_token']}
#     response = get(api_url + "me/playlists", headers=headers)
#     return jsonify(response.json())

# @app.route("/refresh-token")
# def refresh_token():
#     if 'refresh_token' in session:

#         if datetime.datetime.now().timestamp() > session['expires_at']:
#             req_body = {
#                 "grant_type": "refresh_token",
#                 "refresh_token": session['refresh_token'],
#                 "client_id": client_id,
#                 "client_secret": client_secret,
#             }

#             response = post(token_url, data=req_body)
#             new_token_info = response.json()

#             session['access_token'] = new_token_info['access_token']
#             session['expires_at']  = datetime.datetime.now().timestamp() 
#             + new_token_info['expires_in']

#         return redirect('/playlists')
    
#     else:
#         return redirect('/login')

if __name__ == "__main__":
    app.run(debug=True, port=8080)