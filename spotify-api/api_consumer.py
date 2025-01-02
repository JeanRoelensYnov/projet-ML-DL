import requests

CLIENT_ID = "bc44d1a9574d43bea2f35a12b563fce6"
CLIENT_SECRET = "" # Ask for secret if necessary
tracks = [
    {"track": 'Shine on you crazy diamond', "artist": "Pink Floyd"},
    {"track": 'Kashmir', "artist": "Led Zeppelin"}
]


def get_spotify_token(client_id: str, client_secret: str):
    url = "https://accounts.spotify.com/api/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": f"{client_id}",
        "client_secret": f"{client_secret}"
    }
    response = requests.post(
        url, data)
    response.raise_for_status()
    return response.json()["access_token"]


def search_track(track_name: str, artist_name: str, token: str):
    url = "https://api.spotify.com/v1/search"
    headers = {"Authorization": f"Bearer {token}"}
    query = track_name
    if artist_name:
        query += f" artist:{artist_name}"
    params = {"q": query, "type": "track", "limit": 1}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    items = response.json()["tracks"]["items"]
    if items:
        track = items[0]
        return {
            "id": track["id"],
            "name": track["name"],
            "artist": ", ".join(artist["name"] for artist in track["artists"]),
            "explicit": track["explicit"]
        }
    return None


def get_audio_features(track_id: str, token: str):
    url = f"https://api.spotify.com/v1/audio-features/{track_id}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Error {response.status_code}: {response.json()}")
    response.raise_for_status()
    return response.json()


def get_track_details_and_features(track_name: str, artist_name: str) -> str | dict:
    token = get_spotify_token(CLIENT_ID, CLIENT_SECRET)
    track = search_track(track_name, artist_name, token)
    if not track:
        return f"Track '{track_name}' by '{artist_name}' not found."
    features = get_audio_features(track['id'], token)

    details = {
        "name": track["name"],
        "artist": track["artist"],
        "explicit": track["explicit"],
        "danceability": features["danceability"],
        "energy": features["energy"],
        "key": features["key"],
        "loudness": features["loudness"],
        "mode": features["mode"],
        "speechiness": features["speechiness"],
        "acousticness": features["acousticness"],
        "instrumentalness": features["instrumentalness"],
        "liveness": features["liveness"],
        "valence": features["valence"],
        "tempo": features["tempo"],
        "time_signature": features["time_signature"]
    }

    return details


if __name__ == "__main__":
    for t in tracks:
        details = get_track_details_and_features(t["track"], t["artist"])
        print(details)
        input()
