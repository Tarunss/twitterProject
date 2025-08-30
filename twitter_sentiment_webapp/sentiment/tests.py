from django.test import TestCase
from .models import SentimentAnalysis

class SentimentAnalysisModelTest(TestCase):
    def setUp(self):
        SentimentAnalysis.objects.create(tweet_id='12345', sentiment_score=0.75)
        SentimentAnalysis.objects.create(tweet_id='67890', sentiment_score=-0.25)

    def test_sentiment_analysis_creation(self):
        sentiment = SentimentAnalysis.objects.get(tweet_id='12345')
        self.assertEqual(sentiment.sentiment_score, 0.75)

    def test_sentiment_analysis_negative_score(self):
        sentiment = SentimentAnalysis.objects.get(tweet_id='67890')
        self.assertEqual(sentiment.sentiment_score, -0.25)

    def test_sentiment_analysis_count(self):
        count = SentimentAnalysis.objects.count()
        self.assertEqual(count, 2)