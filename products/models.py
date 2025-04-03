from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES = [
    ('electronics', '전자기기'),
    ('clothes', '의류'),
    ('books', '책'),
    ('etc', '기타'),
]

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='etc')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class BlockList(models.Model):
    blocker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blocker')
    blocked = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blocked')
    blocked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.blocker.username} → {self.blocked.username}"