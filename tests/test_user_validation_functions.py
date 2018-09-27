from unittest import TestCase
from app.validation import verify_length
from app.validation import verify_age
from app.validation import verify_password
from app.validation import verify_username
from app.validation import verify_email


class TestUserValidation(TestCase):
    """
    Test class for testing user input validation
    """

    def test_valid_name_username_input(self):
        self.assertFalse(verify_username('michael', 'michael'))
        self.assertTrue(verify_username('michael', 'myco'))

    def test_name_length_greater_or_equal_to_four(self):
        self.assertFalse(verify_length('mmm'))
        self.assertTrue(verify_length('namessss'))
        self.assertTrue(verify_length('mmmm'))

    def test_age_takes_an_integer_value(self):
        self.assertTrue(verify_age(2))
        self.assertFalse(verify_age('2'))

    def test_age_cannot_be_zero(self):
        self.assertFalse(verify_age(0))

    def test_valid_password_contains_uppercase_letter(self):
        self.assertTrue(verify_password('E3m@'))
        self.assertFalse(verify_password('3cm@'))

    def test_valid_password_contains_lowercase_letter(self):
        self.assertTrue(verify_password('E3m@'))
        self.assertFalse(verify_password('3MM@'))

    def test_valid_password_contains_a_digit(self):
        self.assertTrue(verify_password('E3m@'))
        self.assertFalse(verify_password('cMM@'))

    def test_valid_password_contains_special_character(self):
        self.assertTrue(verify_password('E3m@'))
        self.assertFalse(verify_password('cM6g'))

    def test_valid_email_address(self):
        self.assertTrue(verify_email('me@mail.com'))
        self.assertFalse(verify_email('megmail.com'))
