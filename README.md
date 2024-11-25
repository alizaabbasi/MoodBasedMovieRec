# 🎬 Mood-Based Movie Recommendation System

This project is a **Streamlit-based web application** that recommends movies based on the user's mood. It combines sentiment analysis, emoji-based input, and The Movie Database (TMDb) API to deliver tailored movie suggestions.

## Features
- **Emoji-based Mood Input**: Users select their mood using predefined emojis with labels (e.g., 😄 Happy, 😢 Sad, 😠 Angry, 😐 Neutral).
- **Dynamic Sentiment Analysis**: Moods are mapped to sentiments (Positive, Negative, Neutral) with varying confidence levels.
- **Movie Recommendations**: Provides up to 5 movie recommendations based on the detected sentiment using the TMDb API.
- **Confidence Visualization**: Displays a bar chart to visualize the confidence score for the detected sentiment.

## Tech Stack
### Frontend
- Streamlit

### Backend
- Sentiment analysis using TextBlob
- Movie data fetched via TMDb API
- Programming Language: Python
- Visualization: Matplotlib

## Installation
### Prerequisites
- Python 3.7 or higher
- Required libraries: streamlit, textblob, requests, matplotlib
### Setup
- Clone the repository
- Install dependencies
### Get a TMDb API key
- Sign up for an account at TMDb.
- Generate an API key from the Developer section.
- Replace API_KEY in movie_recommendation.py with your TMDb API key.

## File Structure
### app.py
- Main Streamlit application
### sentiment_analysis.py
- Sentiment analysis logic using TextBlob.
### movie_recommendation.py
- Fetches movie data from the TMDb API based on detected sentiment
### requirements.txt
- List of all Python dependencies.

## Usage
- Launch the application.
- Respond to the "How are you feeling today?" prompt by selecting a mood (e.g., 😄 Happy, 😢 Sad).
- Click on the "Get Recommendations" button.
- View:
  - Detected sentiment and confidence level.
  - A bar chart visualizing sentiment confidence.
  - Movie recommendations with details like title, release date, rating, and overview.

## Example Workflow
- User selects 😄 Happy.
- Detected sentiment: Positive (Confidence: 95%).
- Movies recommended from the Comedy genre (e.g., "The Intern," "Toy Story").

## License
- This project is licensed under the MIT License.