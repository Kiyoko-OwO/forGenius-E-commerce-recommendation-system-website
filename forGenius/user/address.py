from user.models import Address_book, User
import jwt
from user.auth import InputError, validate_email as validate_email


def view_address_book(email):
    try:        
        Address_book.objects.filter(user_email=email)
    except:
        pass

def add_address_book(email, address, phone_number):
    if not validate_email(email):
        raise InputError('Invalid Email')        
    try:
        user_email = User.objects.get(pk=email)
    except User.DoesNotExist:
        raise InputError('User not exist')

    reg = Address_book(user_email=user_email, address=address, phone_number= phone_number)
    reg.save()        
    return
    #return view_address_book(email)
