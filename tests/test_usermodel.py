from unittest import TestCase
from app.user import User


class TestcreateUser(TestCase):
    """
    Test class for testing instances of a user
    """
    def setUp(self):
        self.new_user = User('michael', 'myco', 28, 'me@me.com', 'me12345')

    def test_create_user(self):

        self.assertEqual(self.new_user.username, 'myco')
        self.assertEqual(self.new_user.email, 'me@me.com')
        self.assertEqual(self.new_user.password, 'me12345')
        self.assertIsInstance(self.new_user, User)
