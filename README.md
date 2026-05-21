# BookWise - Book Finder & Summarizer 📚✨

A full-stack web application that allows users to search for books by title, fetch detailed information using the Google Books API, and generate AI-powered summaries of book descriptions using the `facebook/bart-large-cnn` model.

## 🚀 Features

- **Book Search**: Instant search for books via the Google Books API.
- **Detailed Metadata**: Retrieves book titles, authors, and full descriptions.
- **AI-Powered Summarization**: Uses a pre-trained BART model to distill long descriptions into concise, meaningful summaries.
- **Clean UI**: A responsive and modern interface for a premium user experience.

## 🛠️ Tech Stack

- **Backend**: [Flask](https://flask.palletsprojects.com/) (Python)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **APIs**: [Google Books API](https://developers.google.com/books)
- **AI/ML**: [Hugging Face Transformers](https://huggingface.co/docs/transformers/index) (`facebook/bart-large-cnn`)

## 📋 Prerequisites

- Python 3.8 or higher
- A Google Cloud Project with the **Books API** enabled
- A Google Books API Key

## ⚙️ Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd "BookWise"
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   Create a `.env` file in the root directory and add your Google Books API key:
   ```env
   GOOGLE_BOOKS_API_KEY=your_api_key_here
   ```

## 📖 Usage

1. **Start the Flask server**:
   ```bash
   python app.py
   ```
2. **Access the application**:
   Open your browser and navigate to `http://localhost:5000`.
3. **Search for a book**:
   Enter a book title in the search bar and click "Search". The app will fetch the details and generate a summary automatically.

> [!NOTE]
> The first time you run the application, it will download the BART model (~1.6GB). This may take several minutes depending on your internet connection.

## 📂 Project Structure

```text
├── services/
│   ├── google_books.py  # Google Books API integration
│   └── summarizer.py    # AI summarization logic
├── static/
│   ├── script.js        # Frontend logic
│   └── style.css        # Custom styling
├── templates/
│   └── index.html       # Main UI template
├── app.py               # Flask application entry point
├── .env                 # Environment variables (Git-ignored)
└── requirements.txt     # Python dependencies
```

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
