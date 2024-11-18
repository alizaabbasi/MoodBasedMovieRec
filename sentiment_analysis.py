from textblob import TextBlob

def get_sentiment(text):
    """Perform sentiment analysis on the input text."""
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity < 0:
        return "Negative"
    else:
        return "Neutral"
    