from bs4 import BeautifulSoup
import requests
import spotipy

Client_ID = "89fe90c56d42499d8a0d4f7b5448fae6"
Client_Secret = "c03ac8c6fede4933ae3b154ba68f8deb"
Redirect_uri = "http://example.com"

spot = spotipy.oauth2.SpotifyOAuth(client_id=Client_ID, client_secret=Client_Secret, redirect_uri=Redirect_uri,
                                   scope="playlist-modify-private")
url = spot.get_authorize_url()
token = spot.get_access_token()
print(url)
page = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
contents = page.text
soup = BeautifulSoup(contents, "html.parser")
names = soup.find_all(name="h3", class_="jsx-4245974604")
names = soup.select("div h3")
print(names)
movies = [name.getText().strip() for name in names].reverse()
print(movies)
