from textblob import TextBlob

def get_sentiment_with_score(text):
    """Perform sentiment analysis on the input text and provide a confidence score."""
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    confidence_score = abs(polarity) * 100  # Convert polarity to a percentage score
    return sentiment, round(confidence_score, 2)

    