from django.db import models
from django.contrib.auth.models import User

class Videos(models.Model):
    video_name = models.CharField(max_length=200)
    video_url = models.URLField()

    def __str__(self):
        return self.video_name

class Comment(models.Model):
    comment_text = models.TextField(blank=False, null=True)
    comment_like = models.PositiveIntegerField(default=0)
    comment_video = models.ForeignKey(Videos, on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_text

# Create your models here.
