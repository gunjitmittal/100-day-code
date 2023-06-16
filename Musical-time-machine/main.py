from pprint import pprint

import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

Client_ID = "89fe90c56d42499d8a0d4f7b5448fae6"
Client_Secret = "c03ac8c6fede4933ae3b154ba68f8deb"
Redirect_uri = "http://example.com"

spot = SpotifyOAuth(client_id=Client_ID, client_secret=Client_Secret, redirect_uri=Redirect_uri,
                    scope="playlist-modify-private")
spot.get_cached_token()
client = spotipy.client.Spotify(oauth_manager=spot)
user_id = client.current_user()["id"]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=Client_ID,
        client_secret=Client_Secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")
url = f"https://www.billboard.com/charts/hot-100/{date}/"
page = requests.get(url)
contents = page.text
soup = BeautifulSoup(contents, "html.parser")
songs = soup.select("li h3")
song_list = [song.getText().strip() for song in songs]

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
uri_list = []
for song in song_list[:100]:
    query = {
        "track": song,
        "year": date.split("-")[0],
    }
    result = sp.search(f"track:{song} year:{date.split('-')[0]}", type="track")
    try:
        uri_list.append(result["tracks"]["items"][0]["uri"])
    except IndexError:
        pass
sp.playlist_add_items(playlist_id=playlist["id"], items=uri_list)
