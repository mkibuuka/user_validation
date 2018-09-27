from unittest import TestCase
from app.validation import validate_user


class TestUserValidations(TestCase):
    """
    Test class for testing user input validation

    """
    def setUp(self):
        self.user_1 = ('michael', 'mico', 18, 'me@gmail.com', 'Mem!12345t')
        self.user_2 = ('mico', 'michael', 0, 'me@gmail.com', 'Mem!12345t')

    def test_successful_user_validation(self):
        self.assertTrue(validate_user(*self.user_1))

    def test_unsuccessful_user_validation(self):
        self.assertEqual(validate_user(name='michael', username='michael', age=25, email='me@gmail.com', password='Mem!12345t'), 'Please provide the correct name and/or username')
        self.assertEqual(validate_user(name='mic', username='michael', age=25, email='me@gmail.com', password='Mem!12345t'), 'Please provide the correct name and/or username')
        self.assertEqual(validate_user(name='michaeal', username='mico', age=0, email='me@gmail.com', password='Mem!12345t'), 'Please provide a valid age')
        self.assertEqual(validate_user(name='michael', username='mico', age=28, email='megmail.com', password='Mem!12345t'), 'invalid email or missing email address')
        self.assertEqual(validate_user(name='michael', username='mico', age=28, email='me@gmail.com', password='Mem12345t'), 'missing password/password should be atleast 4 characters')
