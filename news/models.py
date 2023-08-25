from django.db import models



class NewsData(models.Model):
    name = models.CharField(max_length=30,blank=False)
    title = models.TextField()
    image = models.CharField(max_length=200)
    content = models.TextField()
    time = models.CharField(max_length=80, null=False, blank=False)

    class Meta:
        unique_together = ["time", "image"]
