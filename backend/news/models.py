from django.db import models
from accounts.models import User


class News(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news')
    title = models.CharField(max_length=240)
    title_image = models.ImageField(upload_to='news/')
    body = models.TextField()
    created_at = models.DateField(auto_now_add=True)
