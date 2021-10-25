from django.db import models
from product.models import Product
from user.models import User
from django.db.models.deletion import CASCADE
from django.core.validators import MinValueValidator 

# Create your models here.
class Order(models.Model):
    order_id = models.IntegerField(null = False, blank = False)
    product_id = models.ForeignKey(Product, on_delete=CASCADE)
    user_email = models.ForeignKey(User, on_delete=CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    price = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.IntegerField(validators=[MinValueValidator(1)])
    paid = models.BooleanField(default=False)

    class Meta:

        db_table = 'order'

        unique_together = ("order_id", "product_id", "user_email")

        

class Cart(models.Model):
    user_email = models.ForeignKey(User, on_delete=CASCADE)
    product_id = models.ForeignKey(Product, on_delete=CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])

    class Meta:

        db_table = 'cart'

        unique_together = ("user_email", "product_id")
