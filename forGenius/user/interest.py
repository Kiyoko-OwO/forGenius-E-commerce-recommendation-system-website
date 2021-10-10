from user.models import User, Interest
from user.errors import InputError

def user_interest(email, interest_list):
    try:
        user_email = User.objects.get(pk=email)
    except User.DoesNotExist:
        raise InputError('User not exist')
    
    for interest in interest_list:
        reg = Interest(user_email=user_email, interests=interest)
        reg.save()        

    return