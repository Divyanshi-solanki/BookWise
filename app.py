from flask import Flask, request, jsonify, render_template
from services.google_books import GoogleBooksService
from services.summarizer import SummarizerService
import os
from dotenv import load_dotenv

# Load environment variables from .env if present
load_dotenv()

app = Flask(__name__, 
            static_folder='static',
            template_folder='templates')

# Initialize services
# Lazy initialization of summarizer to speed up app startup if needed, 
# but here we'll do it at start.
google_books_service = GoogleBooksService()
summarizer_service = SummarizerService()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/book', methods=['GET'])
def get_book():
    title = request.args.get('title')
    if not title:
        return jsonify({"error": "Title parameter is required."}), 400

    # 1. Fetch book details
    book_data, status_code = google_books_service.get_book_details(title)
    
    if status_code != 200:
        return jsonify(book_data), status_code

    # 2. Summarize description
    description = book_data.get('description', '')
    summary = summarizer_service.summarize(description)
    
    # 3. Return combined result
    result = {
        "title": book_data['title'],
        "authors": book_data['authors'],
        "description": description,
        "summary": summary
    }
    
    return jsonify(result)

if __name__ == '__main__':
    # Ensure templates and static folders exist (Flask usually expects them)
    # The script will be run from the root directory.
    app.run(debug=True, port=5000)
