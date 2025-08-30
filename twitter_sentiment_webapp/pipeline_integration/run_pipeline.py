from twitter_sentiment_webapp.src.extract.bluesky_extractor import TwitterExtractor
from src.transform.sentiment_analyzer import SentimentAnalyzer
from src.load.postgres_loader import PostgresLoader
from django.conf import settings

def run_pipeline():
    # Step 1: Extract tweets
    extractor = TwitterExtractor()
    tweets = extractor.extract_tweets()

    # Step 2: Analyze sentiment
    analyzer = SentimentAnalyzer()
    sentiment_results = analyzer.analyze_sentiment(tweets)

    # Step 3: Load results into PostgreSQL
    db_config = {
        'dbname': settings.DATABASES['default']['NAME'],
        'user': settings.DATABASES['default']['USER'],
        'password': settings.DATABASES['default']['PASSWORD'],
        'host': settings.DATABASES['default']['HOST'],
        'port': settings.DATABASES['default']['PORT'],
    }
    loader = PostgresLoader(db_config)
    loader.load_data(sentiment_results)
    loader.close_connection()

if __name__ == "__main__":
    run_pipeline()