from django.shortcuts import render
from .models import SentimentAnalysis

def sentiment_list(request):
    sentiments = SentimentAnalysis.objects.all()
    return render(request, 'sentiment/sentiment_list.html', {'sentiments': sentiments})

def sentiment_detail(request, tweet_id):
    sentiment = SentimentAnalysis.objects.get(tweet_id=tweet_id)
    return render(request, 'sentiment/sentiment_detail.html', {'sentiment': sentiment})