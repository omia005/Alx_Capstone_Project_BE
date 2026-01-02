from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    duration = models.CharField(default='0hrs 0mins', max_length=200)
    director = models.CharField(max_length=200)
    poster = models.ImageField(upload_to="posters/", blank=True, null=True)
    
    
    def __str__(self):
        return self.title
