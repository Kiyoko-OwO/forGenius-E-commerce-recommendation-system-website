from django.db import models
from django.db.models.deletion import CASCADE
from django.core.validators import MinValueValidator 

# Create your models here.
class User(models.Model):
    user_email = models.EmailField(unique=True, primary_key=True)
    user_name = models.CharField(max_length=30)
    password = models.CharField(max_length=255)

class Admin(models.Model):
    admin_email = models.EmailField(unique=True, primary_key=True)
    password = models.CharField(max_length=255)
    

class Interest(models.Model):
    user_email = models.ForeignKey(User, on_delete=CASCADE, primary_key=True)
    interests = models.CharField(max_length=255, primary_key=True)

    class Meta:

        db_table = 'interest'

        unique_together = ("user_email", "interests")

class Address_book(models.Model):
    user_email = models.ForeignKey(User, on_delete=CASCADE)
    address_id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=255)
    phone_number = models.IntegerField(max_length=11, validators=[MinValueValidator(1)])



