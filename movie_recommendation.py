import requests

API_KEY = "f05cffbfd00d0731d7d719eb3277ca6e"  
BASE_URL = "https://api.themoviedb.org/3"

def get_movie_recommendations(sentiment, max_results=50):
    """Fetch up to 50 movies with details like release date, rating, and overview."""
    # Map sentiment to TMDB genres
    if sentiment == "Positive":
        genre_id = 35  # Comedy
    elif sentiment == "Negative":
        genre_id = 27  # Horror
    else:
        genre_id = 18  # Drama

    movies = []
    page = 1

    # Looping through multiple pages to get more results
    while len(movies) < max_results:
        # TMDB API endpoint and parameters
        endpoint = f"{BASE_URL}/discover/movie"
        params = {
            "api_key": API_KEY,
            "with_genres": genre_id,
            "sort_by": "popularity.desc",
            "language": "en-US",
            "page": page,
        }

        # Make API request
        response = requests.get(endpoint, params=params)
        if response.status_code == 200:
            data = response.json()
            results = data.get("results", [])

            # Add movies to the list
            for movie in results:
                if len(movies) >= max_results:
                    break
                movies.append({
                    "Title": movie.get("title", "N/A"),
                    "Release Date": movie.get("release_date", "N/A"),
                    "Rating": movie.get("vote_average", "N/A"),
                    "Overview": movie.get("overview", "No overview available.")
                })
        else:
            print(f"Error: Unable to fetch data (Status Code: {response.status_code})")
            break

        page += 1  # Move to the next page for more results

    return movies
