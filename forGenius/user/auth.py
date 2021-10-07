from user.models import User
import jwt
import time
import random
import user.email_robot as email_robot

class InputError(Exception):
    code = 400
    message = 'InputError'

TOKEN_DB = list()
PRIVATE_KEY = 'nLAghlDB8Qec4d6LD5dhV2QvVs3vpDSY'
RESETCODE_DB = dict()

def auth_login(email, password):
    """ 
    auth_login(email, password)
    check and login in the account 
    """
    try:
        email_query = User.objects.get(pk=email)
    except User.DoesNotExist:
        raise InputError('Incorrect email or password')
    if (email_query.password != password):
        raise InputError('Incorrect email or password')
    token = jwt.encode({'email': email, 'time': time.time()}, PRIVATE_KEY, algorithm='HS256')
    TOKEN_DB.append(token)
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

def auth_change_password(token, old_password, new_password):
    email = token_to_email(token)
    if (len(User.objects.get(pk=email).filter(password=old_password)) != 1):
        raise InputError('Incorrect old password')
    if not validate_password(new_password):
        raise InputError('Invalid new password')
    email_query = User.objects.get(pk=email)
    email_query.password = new_password
    email_query.save()
    return True

def auth_reset_password(reset_code, new_password):
    if not validate_password(new_password):
        raise InputError('Invalid new password')
    email = reset_code_to_email(reset_code)
    email_query = User.objects.get(pk=email)
    email_query.password = new_password
    email_query.save()
    return True

def auth_send_reset_code(email):
    if not validate_email(email):
        raise InputError('Invalid email address, please try again')
    try:
        email_query = User.objects.get(pk=email)
    except User.DoesNotExist:
        raise InputError('Not registered yet, please sign up')
    reset_code = RESETCODE_DB.get(email, default=None)
    if reset_code is None:
        reset_code = generate_reset_code()
    RESETCODE_DB.put(email, reset_code)
    name = email_query.values()[0].get('user_name')
    email_robot.send_email(name, email, reset_code)

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

def generate_reset_code():
    reset_code = ''
    for i in range(6):
        reset_code += str(random.choice([random.randrange(10), chr(random.randrange(97, 123))]))
    return reset_code

def reset_code_to_email(reset_code):
    emails = list(RESETCODE_DB.keys())[list(RESETCODE_DB.values()).index(reset_code)]
    if (len(emails) != 1):
        raise InputError('Invalid reset code')
    RESETCODE_DB.pop(emails[0])
    return emails[0]