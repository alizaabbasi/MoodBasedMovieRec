import matplotlib.pyplot as plt
import streamlit as st
from movie_recommendation import get_movie_recommendations

st.title("🎬 Mood-Based Movie Recommendation System")

# Predefined mood options with emojis and confidence scores
mood_options = {
    "😄 Happy": ("Positive", 95),
    "😢 Sad": ("Negative", 15),
    "😠 Angry": ("Negative", 45),
    "😐 Neutral": ("Neutral", 60)
}

# Prompt for mood selection
st.write("How are you feeling today?")
user_mood = st.radio("Select your mood:", list(mood_options.keys()))

if st.button("Get Recommendations"):
    if user_mood:
        # Map emoji to sentiment and confidence score
        sentiment, confidence_score = mood_options[user_mood]

        # Display sentiment analysis results
        st.write(f"Detected Sentiment: **{sentiment}** (Confidence: {confidence_score}%)")

        # Add a bar chart for visualization
        st.subheader("Sentiment Confidence Visualization")
        fig, ax = plt.subplots()
        ax.bar(["Confidence"], [confidence_score], color='blue')
        ax.set_ylim(0, 100)
        ax.set_ylabel("Confidence Score (%)")
        ax.set_title(f"Confidence in '{sentiment}' Sentiment")
        st.pyplot(fig)

        # Get movie recommendations
        movies = get_movie_recommendations(sentiment)
        if movies:
            st.subheader("Recommended Movies:")
            for movie in movies:
                st.markdown(f"### {movie['title']}")
                st.write(f"**Release Date:** {movie['release_date']}")
                st.write(f"**Rating:** {movie['rating']} ⭐")
                st.write(f"**Overview:** {movie['overview']}")
                st.write("---")  # Separator between movies
        else:
            st.write("No recommendations found!")
    else:
        st.error("Please select a mood.")
