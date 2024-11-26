import pandas as pd
import streamlit as st
from movie_recommendation import get_movie_recommendations

def display_movie_list(sentiment):
    """Fetch and display the top 3 movies in detail and the remaining in a table."""
    # Fetch movies
    movies = get_movie_recommendations(sentiment, max_results=50)

    if movies:
        # Convert the list of movies to a pandas DataFrame
        movies_df = pd.DataFrame(movies)

        # Display the top 3 movies in detail
        st.write("### Top 3 Recommended Movies:")
        for i, movie in enumerate(movies[:3]):
            st.markdown(f"### {movie['Title']}")
            st.write(f"**Release Date:** {movie['Release Date']}")
            st.write(f"**Rating:** {movie['Rating']} ⭐")
            st.write(f"**Overview:** {movie['Overview']}")
            st.write("---")  # Separator between movies

        # Display the remaining movies in a table
        st.write("### More Recommended Movies:")
        st.dataframe(movies_df[3:].reset_index(drop=True))  # Display movies 4-50

        # Add a download button for the entire DataFrame
        st.download_button(
            label="Download Full Movie List as CSV",
            data=movies_df.to_csv(index=False),
            file_name='movie_recommendations.csv',
            mime='text/csv'
        )
    else:
        st.error("No recommendations found!")

