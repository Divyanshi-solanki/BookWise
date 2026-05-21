import requests
import os

class GoogleBooksService:
    def __init__(self):
        self.api_key = os.getenv("GOOGLE_BOOKS_API_KEY")
        self.base_url = "https://www.googleapis.com/books/v1/volumes"

    def get_book_details(self, title):
        if not self.api_key:
            return {"error": "API Key not found. Please set GOOGLE_BOOKS_API_KEY environment variable."}, 500

        params = {
            "q": f"intitle:{title}",
            "key": self.api_key,
            "maxResults": 1
        }

        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            data = response.json()

            if "items" not in data or len(data["items"]) == 0:
                return {"error": "Book not found."}, 404

            book_info = data["items"][0]["volumeInfo"]
            
            return {
                "title": book_info.get("title", "Unknown Title"),
                "authors": book_info.get("authors", ["Unknown Author"]),
                "description": book_info.get("description", "No description available.")
            }, 200

        except requests.exceptions.RequestException as e:
            return {"error": f"API request failed: {str(e)}"}, 502
