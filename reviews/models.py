from django.db import models
from products.models import Product
from django.contrib.auth.models import User

# Create your models here.

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False, null=False)
    review_title = models.CharField(max_length=300, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
