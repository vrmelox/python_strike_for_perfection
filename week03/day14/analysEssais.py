from textblob import TextBlob
# Sample text for sentiment analysis
text = "I hate Mondays."
# Create a TextBlob object
blob = TextBlob(text)
# Perform sentiment analysis
sentiment = blob.sentiment
# Print sentiment
print(type(sentiment[0]))