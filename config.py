#will store my API key 
#methods for connecting to the spotify API

# client id 1c2d60ac84e1481bab5fb786102be6ef
# client secret f33c6a393e234937953831d9a8b651e3
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os  #can get variables that are set in the environment (ex my personal computer os)

def getSpotifyClientIDAndSecret():
    client_id = os.getenv("SPOTIPY_CLIENT_ID")
    client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
    
    if not client_id or not client_secret:
        raise ValueError("Please set SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET in your environment variables.")
    
    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    return spotipy.Spotify(auth_manager=auth_manager)

def checkConnection():
    spotify = getSpotifyClientIDAndSecret()
    result = spotify.search(q="Phoebe Bridgers", type="track", limit=1)
    
    if result['tracks']['items']:
        print("Connection successful")
    else:
        print("Connection failed")

checkConnection()