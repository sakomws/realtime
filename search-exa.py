import os
from exa_py import Exa
from dotenv import load_dotenv
import json

# Load environment variables from a .env file (if using one)
load_dotenv()

def get_exa_client():
    """Initialize the Exa client with an API key."""
    api_key = os.getenv("EXA_API_KEY")  # Use env or fallback
    return Exa(api_key=api_key)

def search_hackathons(location: str):
    """
    Search for a list of hackathons happening in a specific location.
    
    Args:
        location (str): The location to search for hackathons (e.g., 'Bay Area').
    
    Returns:
        list: Search results containing relevant tweets about hackathons.
    """
    exa = get_exa_client()
    
    query = f"List of hackathons happening in {location}"
    
    # Perform the search with filters
    result = exa.search_and_contents(
        query=query,
        type="neural",
        use_autoprompt=True,
        num_results=20,
        text=True,
        exclude_domains=["en.wikipedia.org"],
        start_published_date="2023-01-01",
        category="tweet"
    )
    
    # Extract and return the relevant results (assuming a 'results' field)
    return result

if __name__ == "__main__":
    location = input("Enter the location to search for hackathons: ")
    
    try:
        results = search_hackathons(location)
        print(results)
    except Exception as e:
        print(f"Error: {e}")
