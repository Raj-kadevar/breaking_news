from django.db import models



class NewsData(models.Model):
    name = models.CharField(max_length=30,blank=False)
    title = models.TextField()
    image = models.ImageField(max_length=150)
    content = models.TextField()