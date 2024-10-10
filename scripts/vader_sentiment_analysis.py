import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Step 1: Load the Preprocessed Data
df = pd.read_csv('data/processed_news_headlines.csv')

# Step 2: Initialize VADER Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

# Step 3: Define a Function to Get Sentiment Scores
def get_sentiment(text):
    scores = analyzer.polarity_scores(text)
    # Classify based on the compound score
    if scores['compound'] >= 0.05:
        return 'positive'
    elif scores['compound'] <= -0.05:
        return 'negative'
    else:
        return 'neutral'

# Step 4: Apply Sentiment Analysis on the Text Data
# Assuming 'joined_tokens' contains the preprocessed headlines
df['sentiment'] = df['joined_tokens'].apply(get_sentiment)

# Step 5: Show Some Results
print(df[['joined_tokens', 'sentiment']].head())

# Step 6: Save the Results to a New CSV
df.to_csv('./data/news_with_sentiment.csv', index=False)
print("Sentiment analysis completed and saved to 'data/news_with_sentiment.csv'")
