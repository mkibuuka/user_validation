from unittest import TestCase
from app.validation import is_valid_length
from app.validation import is_valid_age
from app.validation import is_valid_password
from app.validation import is_valid_name_or_username
from app.validation import is_valid_email


class TestUserValidation(TestCase):
    """
    Test class for testing user input validation
    """

    def test_valid_name_username_input(self):
        self.assertFalse(is_valid_name_or_username('michael', 'michael'))
        self.assertTrue(is_valid_name_or_username('michael', 'myco'))

    def test_name_length_greater_or_equal_to_four(self):
        self.assertFalse(is_valid_length('mmm'))
        self.assertTrue(is_valid_length('namessss'))
        self.assertTrue(is_valid_length('mmmm'))

    def test_age_takes_an_integer_value(self):
        self.assertTrue(is_valid_age(2))
        self.assertFalse(is_valid_age('2'))

    def test_age_cannot_be_zero(self):
        self.assertFalse(is_valid_age(0))

    def test_valid_password_contains_uppercase_letter(self):
        self.assertTrue(is_valid_password('E3m@'))
        self.assertFalse(is_valid_password('3cm@'))

    def test_valid_password_contains_lowercase_letter(self):
        self.assertTrue(is_valid_password('E3m@'))
        self.assertFalse(is_valid_password('3MM@'))

    def test_valid_password_contains_a_digit(self):
        self.assertTrue(is_valid_password('E3m@'))
        self.assertFalse(is_valid_password('cMM@'))

    def test_valid_password_contains_special_character(self):
        self.assertTrue(is_valid_password('E3m@'))
        self.assertFalse(is_valid_password('cM6g'))

    def test_valid_email_address(self):
        self.assertTrue(is_valid_email('me@mail.com'))
        self.assertFalse(is_valid_email('megmail.com'))
