from django.db import models
from accounts.models import User
from products.models import Product


class Mark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='marks')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='marks')

    def __str__(self):
        return f'{str(self.user)} marked {self.product}'

    class Meta:
        ordering = ('-id',)
