from django.db import models
from django.conf import settings  # لجلب موديل المستخدم

class Product(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  #  هيك بنربط بأي موديل مستخدم مخصص
        on_delete=models.CASCADE,
        related_name='products'
    )
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

