from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()
    extra_quantity = models.IntegerField(default=0)

    total_amount = models.FloatField(editable=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.total_amount = self.price * (self.quantity + self.extra_quantity)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.product_name
