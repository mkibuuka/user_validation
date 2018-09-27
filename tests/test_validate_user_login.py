from unittest import TestCase
from app.validation import validate_user_login


class TestUserValidations(TestCase):
    """
    Test class for testing user input validation

    """
    def setUp(self):
        self.user_1 = ('me@gmail.com', 'Mem!12345t')
        self.user_2 = ('megmail.com', 'Mem!12345t')
        self.user_3 = ('me@gmail.com', 'Me2')

    def test_successful_user_login(self):
        self.assertTrue(validate_user_login(*self.user_1))

    def test_unsuccessful_user_login(self):
        self.assertEqual(validate_user_login(*self.user_2), 'invalid email or missing email address')
        self.assertEqual(validate_user_login(*self.user_3), 'missing password/password should be atleast 4 characters')
