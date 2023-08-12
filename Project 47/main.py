import os

import requests
import bs4
import spotipy
import spotipy as spotipy
from spotipy import SpotifyClientCredentials, SpotifyOAuth

# #############################################################################################################
userInput_date = input("Enter the date Which you want to listen YYYY-MM-DD: ")
URL = "https://www.billboard.com/charts/hot-100/" + userInput_date

response = requests.get(url=URL)
data = response.text

soup = bs4.BeautifulSoup(data, 'html.parser')

class_alpha = "c-title  a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet"
class_99_song = "c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only"

first_song = soup.find_all(name="h3", id="title-of-a-story", class_="c-title")[6:7]
row_all_songs = first_song + soup.find_all(name="h3", id="title-of-a-story", class_=class_99_song)

all_songs = [' '.join(song.getText().split()) for song in row_all_songs]


with open("100_song.txt", "w", encoding="utf-8") as file:
    for song in all_songs:
        file.write(song)

# print(all_songs)
#############################################################################################################
# # API------------------------------------------------------
# sp = spotipy.SpotifyOAuth(client_id=os.environ.get("CLIENT_ID"), client_secret=os.environ.get("CLIENT_SECRET_KEY"), redirect_uri="http://example.com")
# sp.get_access_token()
# acces_token = "https://example.com/?code=AQB_aJ4UKcPGGlKEZA9ql6RW8rUJQz0pY4M7Uaz7NMqHgznQE0VqVWNcHTqhmDE1O7eBdi9SBvBs4XJ9t9mp5E8ToG2eduyrXTIGIfz4J3cAeWM1eSV0abTerbTs1L2w8mrPA2rm3ZaXYaItULUzTLIaDqq82g"
# tokens = {"access_token": "BQA3AEbUhN0MevRc5kTw2prmdyMocfVd4yngfcZ-GDEPiqIunsrgnqv78TPypOO-xNIdabQTbgSspBHN3fa9y1VtrzZqQs8V-RI17oIvE-vb3O9qsQUVlSCNX8LNsTt0muoiVrHmwQoXz7xZNQoa4FkmeyfjzqRwR5UYRVuAF1fSLWwy-7GMbbj2MiUMo90keNAu7Q", "token_type": "Bearer",  "refresh_token": "AQCmX5DlxBTwv1OysMZBKVjngEIYzJvH6nMVRFlH2GinliCnXE3Zd2VHRzuYMQvJj-hEiA8dQjpNPt6nLd47OEB0kB0MmCrkrQQ96fqkjfWqYrxC5ZMhKcm31O5tnaEx-Y0"}
# headers = {
#     'Authorization': 'Bearer ' + tokens["access_token"]
# }
#
# response = requests.get('https://api.spotify.com/v1/me', headers=headers)
# print(response.json())
# if response.status_code == 200:
#     # Success!
#     user_id = response.json()['id']
# else:
#     # Error occurred
#     print('Error:', response.status_code)


# sp = spotipy.Spotify(
#     auth_manager=SpotifyOAuth(
#         scope="playlist-modify-private",
#         redirect_uri="http://example.com",
#         client_id=os.environ.get("CLIENT_ID"),
#         client_secret=os.environ.get("CLIENT_SECRET_KEY"),
#         show_dialog=True,
#         cache_path="token.txt"
#     )
# )
# user_id = sp.current_user()["id"]
# name = 'Radiohead'
#
# results = sp.search(q='artist:' + name, type='artist')
# items = results['artists']['items']
# if len(items) > 0:
#     artist = items[0]
#     print(artist['name'], artist['images'][0]['url'])
#     print(user_id)

# headers = {
#     'Authorization': 'Bearer ' + "BQDsl_LLDs7-nVaazy7abYTyRJx7Ihv3t8BUukcdwdOoOBcGJevxdcTgsnX3AnzExOOLagHHVPSZrrG__s_ybr6a86sSWsLWue9sqoIl2l2LWx39vNPE8NDkVdG2xaaWuBrDuHAEZsbGlnwDC6CS20g1v6ecGAMlV6oKOdtNbHcJDZEHGFWM7uvjuJtIW1KnZA6erXqSOx_-kOZShEbpFG-Nks-JJpqJnvYW9A",
#     'Content-Type': 'application/json'
# }
#
# data = {
#     'name': 'Sample Playlist',
#     'public': True
# }
#
# response = requests.post('https://api.spotify.com/v1/me/playlists', headers=headers, json=data)
# response.raise_for_status()
# if response.status_code == 201:
#     # Success!
#     playlist_id = response.json()['id']
# else:
#     # Error occurred
#     print('Error:', response.status_code)
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.environ.get("CLIENT_ID"),
                                               client_secret=os.environ.get("CLIENT_SECRET_KEY"),
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-private",
                                               cache_path="token.txt",
                                               show_dialog=True))
song_uris = []
for song in all_songs:
        result = sp.search(q=f"track:{song} year:{userInput_date.split('-')[0]}", type="track")
        # print(result)
        try:
            uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
        except IndexError:
            print(f"{song} doesn't exist in Spotify. Skipped.")

# print(song_uris)

user_id = sp.current_user()["id"]
playlist = sp.user_playlist_create(user=user_id, name=f"{userInput_date} 100 best songs", public= False, description=f"This is the top 100 song in year {userInput_date}")
print(playlist)
playlist_id = playlist["id"]
sp.playlist_add_items(playlist_id=playlist_id,items=song_uris)