import unittest

class TestUser(unittest.TestCase):

    def test_username_required(self):
        user = User()
        with self.assertRaises(ValidationError):
            user.save()

