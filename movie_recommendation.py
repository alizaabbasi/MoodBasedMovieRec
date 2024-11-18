import requests

API_KEY = "f05cffbfd00d0731d7d719eb3277ca6e"
BASE_URL = "https://api.themoviedb.org/3"

def get_movie_recommendations(sentiment):
    """Fetch movie recommendations based on sentiments."""
    if sentiment == "Positive":
        genre_id = 35 # Comedy
    elif sentiment == "Negative":
        genre_id = 27 # Horror
    else genre_id = 18 # Drama

endpoint = f"{BASE_URL}/discover/movie"
params = {
    "api_key": API_KEY,
    "with_genres": genre_id,
    "sort_by": "popularity.desc",
    "language": "en-US",
    "page": 1
}
response = requests.get(endpoint, params=params)

if response.status_code == 200
     data = response.json()
     return [movie['title'] for movie in data['results'][:5]]
else
    return None

