# Twitter Sentiment Analysis Web Application

This project is a Django web application that integrates with a Twitter sentiment analysis pipeline. It extracts tweets from the Twitter API, analyzes their sentiment, and stores the results in a PostgreSQL database. The application provides a user-friendly interface to view and manage sentiment analysis results.

## Project Structure

```
twitter_sentiment_webapp/
├── manage.py               # Command-line utility for interacting with the Django project
├── README.md               # Documentation for the project
├── requirements.txt        # List of required Python packages
├── twitter_sentiment_webapp/
│   ├── __init__.py        # Marks the directory as a Python package
│   ├── asgi.py            # ASGI configuration for asynchronous server communication
│   ├── settings.py        # Settings and configuration for the Django project
│   ├── urls.py            # URL routing for the Django project
│   └── wsgi.py            # WSGI configuration for the Django project
├── sentiment/
│   ├── __init__.py        # Marks the sentiment directory as a Python package
│   ├── admin.py           # Registers models with the Django admin site
│   ├── apps.py            # Configuration for the sentiment app
│   ├── migrations/         # Directory for database migrations
│   │   └── __init__.py    # Marks the migrations directory as a Python package
│   ├── models.py          # Defines data models for sentiment analysis
│   ├── tests.py           # Test cases for the sentiment app
│   ├── views.py           # View functions for handling requests
│   └── urls.py            # URL routing specific to the sentiment app
├── pipeline_integration/
│   ├── __init__.py        # Marks the pipeline_integration directory as a Python package
│   └── run_pipeline.py     # Logic to run the sentiment analysis pipeline
└── src/
    ├── extract/
    │   └── twitter_extractor.py  # Logic for extracting tweets from the Twitter API
    ├── transform/
    │   └── sentiment_analyzer.py  # Logic for analyzing the sentiment of tweets
    ├── load/
    │   └── postgres_loader.py      # Logic for loading results into PostgreSQL
    ├── utils/
    │   └── helpers.py              # Utility functions for the project
    └── main.py                     # Entry point for running the sentiment analysis pipeline
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd twitter_sentiment_webapp
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```
   pip install -r requirements.txt
   ```

4. **Configure the database settings in `twitter_sentiment_webapp/settings.py`.**

5. **Run database migrations:**
   ```
   python manage.py migrate
   ```

6. **Run the development server:**
   ```
   python manage.py runserver
   ```

## Usage

- Access the web application at `http://127.0.0.1:8000/`.
- Use the admin interface to manage sentiment analysis results.

## License

This project is licensed under the MIT License.