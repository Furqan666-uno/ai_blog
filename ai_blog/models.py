from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    youtube_title= models.CharField(max_length=200)
    youtube_link= models.URLField()
    generated_content= models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    audio_file = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.youtube_title