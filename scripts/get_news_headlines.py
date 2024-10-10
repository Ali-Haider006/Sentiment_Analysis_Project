import requests
import pandas as pd

# Replace 'your_api_key' with your actual NewsAPI key
API_KEY = '66d6ba2399d94092a4a3fc5408bddb68'

# Define the NewsAPI endpoint and query
url = f'https://newsapi.org/v2/everything?q=stocks&language=en&sortBy=publishedAt&apiKey={API_KEY}'

# Make the API request and get the response as JSON
response = requests.get(url).json()

# Extract articles from the response
articles = response.get('articles', [])

# Collect headlines and publication dates
headlines = []
for article in articles:
    headline = article.get('title')
    date_published = article.get('publishedAt')
    headlines.append([headline, date_published])

# Convert the list of headlines to a DataFrame
df = pd.DataFrame(headlines, columns=['headline', 'published_at'])

# Save the DataFrame to a CSV file
# df.to_csv('financial_news_headlines.csv', index=False)
df.to_csv('./data/financial_news_headlines.csv', index=False)

print("News headlines saved to 'financial_news_headlines.csv'")
