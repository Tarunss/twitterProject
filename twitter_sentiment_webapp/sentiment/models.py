from django.db import models

class SentimentAnalysis(models.Model):
    tweet_id = models.CharField(max_length=255, unique=True)
    sentiment_score = models.FloatField()

    def __str__(self):
        return f'Tweet ID: {self.tweet_id}, Sentiment Score: {self.sentiment_score}'