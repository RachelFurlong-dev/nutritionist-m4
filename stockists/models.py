from django.db import models

# Define your models here


class Stockist(models.Model):
    # Define fields for the Stockist model
    name = models.CharField(max_length=50, null=False, blank=False)
    has_stock = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        # String representation of a Stockist object
        return self.name
