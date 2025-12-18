from django.db import models
from django.contrib.auth import User

# Create your models here.
class Movie(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField()
  rating = models.IntegerField()
  director = models.CharField(max_length=200)
  genre = models.CharField(max_length =200)
  image = models.ImageField(default= 'fullback.jpg')

  def __str__(self):
    return self.title

class Review(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews' )
  comment = models.TextField()
  rating = models.IntegerField()

  def __str__(self):
    return self.author