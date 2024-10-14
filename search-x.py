import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the Bearer Token from environment variables
BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN')

if not BEARER_TOKEN:
    raise Exception("Bearer token not found. Make sure to set it in the .env file.")

SEARCH_URL = 'https://api.twitter.com/2/tweets/search/recent'

def create_headers(bearer_token):
    """Create headers for the API request."""
    return {"Authorization": f"Bearer {bearer_token}"}

def search_tweets(query, max_results=10):
    """Search for tweets with a given query and max results."""
    headers = create_headers(BEARER_TOKEN)
    params = {
        'query': query,
        'max_results': max_results,
        'tweet.fields': 'created_at,author_id,text',
        'expansions': 'author_id',
        'user.fields': 'username',
    }

    response = requests.get(SEARCH_URL, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Request failed: {response.status_code}, {response.text}")

def main():
    # Search for tweets with the hashtag #xaihackathon
    try:
        tweets_data = search_tweets('from:AGIHouseSF', max_results=100)
        
        # Print the JSON result in a readable format
        print(json.dumps(tweets_data, indent=4))
        
        # Return the JSON result for further use if needed
        return tweets_data
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
