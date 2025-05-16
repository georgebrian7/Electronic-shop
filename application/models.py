from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/', blank=True)

    def __str__(self):
        return self.name

class ShopItem(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='shop_items')
    type = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='type_items',default=1)
    quantity = models.PositiveIntegerField(default=0)
    session_key = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return self.type.name

