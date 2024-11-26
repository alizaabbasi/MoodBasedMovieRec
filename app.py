import matplotlib.pyplot as plt
import streamlit as st
from movie_list import display_movie_list  # Import from movie_list.py

# Predefined mood options with emojis and confidence scores
mood_options = {
    "😄 Happy": ("Positive", 95),
    "😢 Sad": ("Negative", 15),
    "😠 Angry": ("Negative", 45),
    "😐 Neutral": ("Neutral", 60)
}

st.title("🎬 Mood-Based Movie Recommendation System")

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

        # Call the function from movie_list.py to display the movie list
        display_movie_list(sentiment)
    else:
        st.error("Please select a mood.")
