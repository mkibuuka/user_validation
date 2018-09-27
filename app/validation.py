import re


def verify_length(name):
    if not len(name) >= 4:
        return False
    return True


def verify_username(name, username):
    if not name == username and verify_length(name) is True and verify_length(username) is True:
        return True
    return False


# def verify_name_username(name, username):
#     if not name or not username:
#         return False
#     if not verify_username(name, username):
#         return False
#     if name == '' or name.isspace() or username == '' or username.isspace:
#         return False
#     return True


def verify_age(age):
    if isinstance(age, str) or age == 0:
        return False
    return True


def verify_password(password):
    if re.match(r"(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@$&]).{4}", password) is None:
        return False
    return True


def verify_email(email):
    if re.match(r"\w+@[a-zA-Z_]+?\.[a-zA-Z]", email) is None:
        return False
    return True


def validate_user(name, username, age, email, password):
    """This function should be called to validate
    provided sign-up form arguments

    Arguments:
        name {[str]} -- user's name
        age {[str]} -- user's age
        username {[str]} -- user's username
        email {[str]} -- user's email address
        password {[str]} -- user's password
    Returns:
        [bool] -- returns True if all values are valid
    """

    if not verify_username(name, username):
        return 'Please provide the correct name and/or username'
    if not verify_age(age):
        return 'Please provide a valid age'
    if not verify_email(email):
        return 'invalid email or missing email address'
    if not verify_password(password):
        return 'missing password/password should be atleast 4 characters'
    return True


def validate_user_login(email, password):
    """
    This function should be called to validate
    user login form arguments

    Arguments:
        username {[str]} -- user's name
        password {[str]} -- user's password
    Returns:
        [bool] -- returns True if all values are valid
    """

    if not verify_email(email):
        return 'invalid email or missing email address'
    if not verify_password(password):
        return 'missing password/password should be atleast 4 characters'

    return True
