from django.db import models

class MyWatchlist(models.Model):
    watched = models.CharField(max_length=30)
    title = models.TextField()
    rating = models.CharField(max_length=5)
    release_date = models.CharField(max_length=50)
    review = models.TextField()