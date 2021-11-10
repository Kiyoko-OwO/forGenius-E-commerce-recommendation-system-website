from django.contrib import admin
from .models import User, Admin, Address_book, Interest

# Register your models here.
admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Address_book)
admin.site.register(Interest)
