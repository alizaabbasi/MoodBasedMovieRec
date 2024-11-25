import requests

API_KEY = "f05cffbfd00d0731d7d719eb3277ca6e"
BASE_URL = "https://api.themoviedb.org/3"

def get_movie_recommendations(sentiment):
    """Fetch movie recommendations with details like release date, rating, and overview."""
    # Map sentiment to TMDB genres
    if sentiment == "Positive":
        genre_id = 35  # Comedy
    elif sentiment == "Negative":
        genre_id = 27  # Horror
    else:
        genre_id = 18  # Drama

    # TMDB API endpoint and parameters
    endpoint = f"{BASE_URL}/discover/movie"
    params = {
        "api_key": API_KEY,
        "with_genres": genre_id,
        "sort_by": "popularity.desc",
        "language": "en-US",
        "page": 1
    }

    # Make API request
    response = requests.get(endpoint, params=params)

    if response.status_code == 200:
        data = response.json()
        if 'results' in data and data['results']:  # Check if results exist
            # Extract relevant details for each movie
            movies = [
                {
                    "title": movie["title"],
                    "release_date": movie.get("release_date", "N/A"),
                    "rating": movie.get("vote_average", "N/A"),
                    "overview": movie.get("overview", "No overview available.")
                }
                for movie in data["results"][:5]  # Limit to top 5 movies
            ]
            return movies
        else:
            return [{"title": "No movies found for this sentiment."}]
    else:
        return [{"title": f"Error: Unable to fetch data (Status Code: {response.status_code})"}]
