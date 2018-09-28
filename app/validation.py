import re


def is_valid_length(name):
    return len(name) >= 4


def is_valid_name_or_username(name, username):
    return name != username and is_valid_length(name) and is_valid_length(username)


def is_valid_age(age):
    return isinstance(age, int) and age > 0


def is_valid_password(password):
    return re.match(r"(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@$&]).{4}", password) is not None


def is_valid_email(email):
    return re.match(r"\w+@[a-zA-Z_]+?\.[a-zA-Z]", email) is not None


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

    if not is_valid_name_or_username(name, username):
        return 'Please provide the correct name and/or username'
    if not is_valid_age(age):
        return 'Please provide a valid age'
    if not is_valid_email(email):
        return 'invalid email or missing email address'
    if not is_valid_password(password):
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

    if not is_valid_email(email):
        return 'invalid email or missing email address'
    if not is_valid_password(password):
        return 'missing password/password should be atleast 4 characters'

    return True
