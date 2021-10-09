from django.contrib import admin

# Register your models here.
from .models import User, Admin, Address_book, Interest

admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Address_book)
admin.site.register(Interest)