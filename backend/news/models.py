from django.db import models
from accounts.models import User


class News(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news')
    title = models.CharField(max_length=240)
    title_image = models.ImageField(upload_to='news/', null=True, blank=True)
    title_video = models.FileField(upload_to='news/', null=True, blank=True)
    body = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-id']
