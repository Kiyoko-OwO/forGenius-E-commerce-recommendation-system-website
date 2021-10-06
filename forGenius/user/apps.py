from django.apps import AppConfig

from user.models import User
import jwt
import time

class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'

TOKEN_DB = list()
PRIVATE_KEY = 'nLAghlDB8Qec4d6LD5dhV2QvVs3vpDSY'

def auth_login(email, password):
    """ 
    auth_login(email, password)
    check and login in the account 
    """
    try:
        email_query = User.objects.get(pk=email)
    except User.DoesNotExist:
        raise InputError('Incorrect email or password')
    if (len(email_query.filter(password=password)) != 1):
        raise InputError('Incorrect email or password')
    token = jwt.encode({'email': email, 'time': time.time()}, PRIVATE_KEY, algorithm='HS256')
    TOKEN_DB.add(token)
    return token

def auth_logout(token):
    """ 
    auth_logout(token)
    logout the current user(token) 
    """
    if token in TOKEN_DB:
        TOKEN_DB.remove(token)
    return True

def auth_register(email, name, password):
    """ 
    auth_register(email, name, password)
    register the account in the database 
    """
    if not validate_email(email):
        raise InputError('Invalid Email')
    try:
        User.objects.get(pk=email)
    except User.DoesNotExist:
        if not validate_name(name):
            raise InputError('Invalid username')
        if not validate_password(password):
            raise InputError('Invalid password')
        reg = User(user_email=email, user_name=name, password=password)
        reg.save()
        return auth_login(email, password)
    raise InputError('Already registered, please log in')

def validate_email(email):
    return True

def validate_name(name):
    if len(name) < 6 or len(name) > 12:
        return False
    return True

def validate_password(password):
    if len(password) < 6 or len(password) > 12:
        return False
    flag = [0, 0, 0]
    for ch in password:
        if ch.isupper():
            flag[0] = 1
        elif ch.islower():
            flag[1] = 1
        elif ch.isdigit():
            flag[2] = 1
        else:
            return False
    if sum(flag) < 3:
        return False
    return True

def check_login(token):
    if token in TOKEN_DB:
        return True
    return False

def token_to_email(token):
    # check token is valid or tamperd
    if not check_login(token):
        raise InputError('Invalid token')
    data = jwt.decode(token, PRIVATE_KEY, algorithms=["HS256"])
    return data['email']
