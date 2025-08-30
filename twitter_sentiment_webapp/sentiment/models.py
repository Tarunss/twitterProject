from django.db import models

class SentimentAnalysis(models.Model):
    tweet_id = models.CharField(max_length=255, unique=True)
    sentiment_score = models.FloatField()

    def __str__(self):
        return f'Tweet ID: {self.tweet_id}, Sentiment Score: {self.sentiment_score}'
    
class Person(models.Model):
    name = models.CharField(max_length=255)
    user = models.CharField(max_length=255, unique = True)
    # We've already defined the related name as a foreign key on Post

class Post(models.Model):
    post_id = models.CharField(max_length=255, unique=True)
    author = models.CharField(max_length=255)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='posts')
    text = models.TextField()
    created_at = models.DateTimeField()
    sentiment = models.ForeignKey()