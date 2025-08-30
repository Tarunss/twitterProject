class SentimentAnalyzer:
    def __init__(self):
        from textblob import TextBlob

    def analyze_sentiment(self, tweet):
        analysis = TextBlob(tweet)
        sentiment_score = analysis.sentiment.polarity
        return {
            'tweet_id': tweet.id,
            'sentiment_score': sentiment_score
        }

    def analyze_batch(self, tweets):
        results = []
        for tweet in tweets:
            result = self.analyze_sentiment(tweet.text)
            results.append(result)
        return results