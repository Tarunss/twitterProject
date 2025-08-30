def calculate_sentiment_score(sentiment_results):
    total_score = sum(result['sentiment_score'] for result in sentiment_results)
    average_score = total_score / len(sentiment_results) if sentiment_results else 0
    return average_score

def format_tweet_data(tweet):
    return {
        'tweet_id': tweet.id,
        'text': tweet.text,
        'created_at': tweet.created_at,
    }

def log_message(message):
    import logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info(message)