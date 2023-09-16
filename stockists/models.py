from django.db import models

# Create your models here.
class Stockist(models.Model):
    business_type = models.CharField(max_length=50, null=False, blank=False)
    in_stock = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.business_type