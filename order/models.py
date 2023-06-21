from django.db import models

# Create your models here.
class Order(models.Model):
    name = models.CharField(max_length=32)
    order_number = models.PositiveIntegerField()
    order_total = models.DecimalField(max_digits=6,decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(auto_now_add=True)
    payment_options= models.CharField(max_length= 32)
    
    def __str__(self):
        return self.name
    
