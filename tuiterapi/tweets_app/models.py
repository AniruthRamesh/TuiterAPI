from django.db import models

class Tuit(models.Model):
    avatar = models.CharField(max_length=255, blank=True, null=True)
    userName = models.CharField(max_length=255, blank=True, null=True)
    handle = models.CharField(max_length=255, blank=True, null=True)
    isTweetImage = models.BooleanField(default=False)
    tweetImage = models.CharField(max_length=255, blank=True, null=True)
    timings = models.CharField(max_length=255, blank=True, null=True)
    comments = models.IntegerField(default=0)
    retweets = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    tuits = models.CharField(max_length=255, blank=True, null=True)
    isContentBelowPost = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    gold = models.BooleanField(default=False)
    retweet = models.BooleanField(default=False)
    retweetBy = models.CharField(max_length=255, blank=True, null=True)
    liked = models.BooleanField(default=False)
    dislikes = models.IntegerField(default=0)
    disliked = models.BooleanField(default=False)

    class Meta:
        db_table = 'tuits'
