from django.db import models

# Create your models here.
class Stockist(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    has_stock = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.name