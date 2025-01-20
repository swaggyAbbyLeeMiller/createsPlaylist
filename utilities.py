#used to find the top songs by stream count

import spotipy


def getTop15Songs(spotify, artistsName):
    try:
        artistID = getTopArtistID(spotify, artistsName)
        return getTracks(artistID)

    except Exception as e:
        apiErrors()
        return []

def getTopArtistID(spotify, artistsName):
    retVal  = spotify.search(q = f"artist:{artistsName}", type = "artist", limit = 1)

    if retVal['artists']['items']:
        return retVal['artists']['items'][0]['id']
    else:
        return ValueError("No artist found, sigh! Try another artist (Like Phoebe Bridgers)")


def getTracks(spotify, artist):
    retVal = spotify.artist_top_tracks(artist)
    tracks = []
    for track in retVal['tracks'][:15]:
        tracks.append({
            'name':  track['name'], 'popularity': track['popularity'], 'url': track['url']})
    return tracks



def apiErrors():
    print("API Error: This isn't very cool!")
