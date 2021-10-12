from django.db import models
from django.db.models.deletion import CASCADE
from user.models import Admin
from django.core.validators import MinValueValidator 

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.CharField(max_length=10000000)
    warranty = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    delivery_date = models.DateField(blank = True, auto_now=False, auto_now_add=False)
    sales_data = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    admin_email = models.ForeignKey(Admin, on_delete=CASCADE)
    price = models.IntegerField(validators=[MinValueValidator(0)], default=0)

class Features(models.Model):
    product_id = models.ForeignKey(Product, on_delete=CASCADE)
    feature = models.CharField(max_length=30)

    class Meta:

        db_table = 'features'

        unique_together = ("product_id", "feature")

