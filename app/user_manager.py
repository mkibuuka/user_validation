from app.user import User
from app.validation import validate_user
from app.validation import validate_user_login


class UserManager(object):
    """
    Manager class for handling and storing user data
    """
    def __init__(self):
        self.users = {}

    def signUp(self, user):
        if validate_user(name=user.name, username=user.username, age=user.age, email=user.email, password=user.password) is True:
            if self.check_if_user_exists(user.email) is False:
                self.insert_user(user)
                return user.username + ' has successfully signed up'
            return 'user with ' + user.email + ' already exists'

    def login(self, user):
        validation = validate_user_login(user.email, user.password)
        if validation is True:
            registered_user = self.get_user_by_email(user.email)
            if isinstance(registered_user, User):
                registered_user.active = True
                return True
        return validation

    # check if user exits based on an email address
    def check_if_user_exists(self, email):
        """[summary]
        """
        try:
            self.users[email]
            return 'user with ' + email + ' already exists'

        except KeyError:

            return False

    def insert_user(self, user):
        self.users[user.email] = user

    def get_user_by_email(self, email):

        try:
            return self.users[email]

        except KeyError as e:
            return e

    def get_all_users(self):
        return [v for v in self.users.values()]

# create an instance of user_manager
user_manager = UserManager()
