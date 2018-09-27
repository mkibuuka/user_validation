from unittest import TestCase
from app.user_manager import user_manager
from app.user import User


class TestUserManager(TestCase):
    """
    Test class for manupilations on the user model class
    """
    def setUp(self):
        user_data = ('michael', 'mico', 18, 'me@gmail.com', 'Mem!12345t')
        user_dataa = ('ivans', 'kibuuks', 28, 'kibuu@gmail.com', 'tRy!@78645r')
        login_data = ('travis', 'painfull', 58, 'trygmail.com', 'tRy!@78645r')
        self.user_1 = User(*user_data)
        self.user_2 = User(*user_dataa)
        self.user_3 = User(*login_data)

    def test_successful_new_user_signup(self):
        self.assertEqual(user_manager.signUp(self.user_1), 'mico has successfully signed up')
        self.assertEqual(len(user_manager.users), 1)

    def test_unsuccessful_new_user_signup(self):
        self.assertEqual(user_manager.signUp(self.user_1), 'user with me@gmail.com already exists')

    def test_to_get_user_by_email(self):
        self.assertEqual(user_manager.signUp(self.user_2), 'kibuuks has successfully signed up')
        self.assertEqual(len(user_manager.users), 2)
        self.assertIsInstance(user_manager.get_user_by_email(self.user_2.email), User)

    def test_to_get_user_by_email_unsuccessful(self):
            person = user_manager.get_user_by_email('mycovan@g.com')
            self.assertIsInstance(person, KeyError)

    def test_to_to_get_all_users_successful(self):
        self.assertIsInstance(user_manager.get_all_users(), list)
        self.assertEqual(len(user_manager.get_all_users()), 2)

    def test_to_to_to_successfully_login_user(self):
        self.assertTrue(user_manager.login(self.user_1))

    def test_to_to_to_unsuccessfully_login_user(self):
        self.assertEqual(user_manager.login(self.user_3), 'invalid email or missing email address')
