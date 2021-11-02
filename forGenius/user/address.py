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
            "address_line" : book.address_line,
            "post_code": book.post_code,
            "suburb": book.suburb,
            "state": book.state,
            "country": book.country,
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

def edit_address_book(email, name, address_line, post_code, suburb, state, country, phone_number, address_id):
    # check user authorization (potential attack: one user edit another user's address)
    try:
        info = Address_book.objects.get(address_id=address_id)
    except Address_book.DoesNotExist:
        raise InputError('Address book exist')
    info.name = name
    info.address_line = address_line
    info.post_code = post_code
    info.suburb = suburb
    info.state = state
    info.country = country
    info.phone_number = phone_number 
    info.save()
    # return view_address_book(email)

def add_address_book(email, name, address_line, post_code, suburb, state, country, phone_number):
    try:
        user_email = User.objects.get(pk=email)
    except User.DoesNotExist:
        raise InputError('User not exist')
    reg = Address_book(user_email=user_email, name=name, address_line=address_line, 
                        post_code=post_code, suburb=suburb, state=state, country=country, 
                        phone_number= phone_number)
    reg.save()        
    # return view_address_book(email)


def address_book_detail(token, email, address_id):
    try:
        info = Address_book.objects.get(address_id=address_id)
    except Address_book.DoesNotExist:
        raise InputError('User not exist')
    data = {
            "token" : token,
            "address" : info.address,
            "name" : info.name,
            "address_line" : info.address_line,
            "post_code": info.post_code,
            "suburb": info.suburb,
            "state": info.state,
            "country": info.country,
            "phone_number" : info.phone_number,
            "address_id" : info.address_id,
        } 
    return data
