import streamlit as st
from sentiment_analysis import get_sentiment
from movie_recommendation import get_movie_recommendations

st.title("🎬 Mood-Based Movie Recommendation System")


# User input for mood description
user_input = st.text_area("How are you feeling today?", placeholder="Describe your mood...")

if st.button("Get Recommendations"):
    if user_input:
        sentiment = get_sentiment(user_input)
        st.write(f"Detected Sentiment: **{sentiment}**")

        # Get movie recommendations
        movies = get_movie_recommendations(sentiment)
        if movies:
            st.subheader("Recommended Movies:")
            for movie in movies:
                st.write(f"- {movie}")
        else:
            st.write("No recommendations found!")
    else:
        st.error("Please enter a description of your mood.")
