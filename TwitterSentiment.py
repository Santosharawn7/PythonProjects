# Importing the Tweepy library to interact with the Twitter API
import tweepy
# Importing TextBlob library to perform sentiment analysis on tweets
from textblob import TextBlob

# Twitter API credentials (Keys and Tokens) - these are required to authenticate your application
consumer_key = "V3pScVRIRUJTVU9JZlpIZkxvczA6MTpjaQ"
consumer_secret = "LRp6X84UTuPnXzMREivnDhnBbjhICs-3Sr1iNyR0X4SRJAzE2W"

access_token = "759265089979576322-cxD3OXXQfYslbU7qXuXr4l6jnCxaWEH"
access_token_secret = "afCI65pzVPmDNqd1WWDyHNxDS2rj3Q4ePwdlyR7FvHezg"


# Function to fetch tweets based on a specific keyword
def fetch_tweets(keyword):
    # Step 1: Authenticate using consumer key and secret
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Step 2: Creating an API object using authenticated credentials
    # wait_on_rate_limit=True ensures that the app handles Twitter API rate limits gracefully
    api = tweepy.API(auth, wait_on_rate_limit=True)

    try:
        # Step 3: Searching for tweets that contain the given keyword (limited to 10 tweets, in English)
        public_tweets = api.search_tweets(q=keyword, count=10, lang="en")

        # Step 4: Loop through each tweet and perform sentiment analysis
        for tweet in public_tweets:
            # Printing the text of the tweet
            print(f'Tweet: {tweet.text}')

            # Analyzing the sentiment of the tweet using TextBlob
            analysis = TextBlob(tweet.text)

            # TextBlob returns two values: polarity (-1 to 1) and subjectivity (0 to 1)
            print(f'Sentiment: {analysis.sentiment}')  # Displaying the sentiment analysis result

    # Handling exceptions, particularly errors returned by the Tweepy library
    except tweepy.TweepError as e:
        print(f"Error: {e}")


# This block executes the fetch_tweets function if the script is run directly
if __name__ == '__main__':
    # Define the keyword you want to search tweets for (in this case 'Trump')
    keyword = 'Trump'  # You can replace 'Trump' with any keyword of interest
    fetch_tweets(keyword)
