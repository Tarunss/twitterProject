class PostgresLoader:
    def __init__(self, db_config):
        from django.db import connection
        self.db_config = db_config

    def load_data(self, sentiment_results):
        from sentiment.models import SentimentAnalysis
        for result in sentiment_results:
            sentiment_record = SentimentAnalysis(
                tweet_id=result['tweet_id'],
                sentiment_score=result['sentiment_score']
            )
            sentiment_record.save()

    def close_connection(self):
        connection.close()