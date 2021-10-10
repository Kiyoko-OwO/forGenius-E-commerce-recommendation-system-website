from user.models import Address_book, User
from user.auth import InputError

def view_address_book(email):
    try:        
        books = Address_book.objects.filter(user_email=email)
    except:
        pass
    data = {"address_book" : []}
    for book in books:
        info = {
            "address_id" : book.address_id,
            "name" : book.name,
            "address" : book.address,
            "phone_number" : book.phone_number
        } 
        data["address_book"].append(info)
    return data

def delete_address_book(email, address_id):
    # check user authorization (potential attack: one user delete another user's address)
    try:
        address = Address_book.objects.get(address_id=address_id)
    except Address_book.DoesNotExist:
        raise InputError('Address ID not exist')
    address.delete()
    # return view_address_book(email)

def edit_address_book(token, email, name, address, phone_number, address_id):
    # check user authorization (potential attack: one user edit another user's address)
    try:
        info = Address_book.objects.get(address_id=address_id)
    except User.DoesNotExist:
        raise InputError('User not exist')
    info.name = name
    info.address = address
    info.phone_number = phone_number 
    info.save()
    data = {
            "token" : token,
            "address_id" : info.address_id,
        } 
    return data
    # return view_address_book(email)

def add_address_book(email, name, address, phone_number):
    try:
        user_email = User.objects.get(pk=email)
    except User.DoesNotExist:
        raise InputError('User not exist')
    reg = Address_book(user_email=user_email, name=name, address=address, phone_number= phone_number)
    reg.save()        
    # return view_address_book(email)
