from user.models import Address_book, User
from user.auth import InputError, validate_email as validate_email


def view_address_book(email):
    try:        
        Address_book.objects.filter(user_email=email)
    except:
        pass

def add_address_book(email, name, address, phone_number):
    try:
        user_email = User.objects.get(pk=email)
    except User.DoesNotExist:
        raise InputError('User not exist')
    reg = Address_book(user_email=user_email, name=name, address=address, phone_number= phone_number)
    reg.save()        
    #return view_address_book(email)
