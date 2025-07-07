import unittest
from backend.schemas import UserSchema

class TestValidation(unittest.TestCase):

    def setUp(self):
        self.user_schema = UserSchema()

    def test_valid_user_data(self):
        valid_data = {
            "email": "test@example.com",
            "password": "SecurePassword123"
        }
        result = self.user_schema.load(valid_data)
        self.assertEqual(result["email"], valid_data["email"])
        self.assertEqual(result["password"], valid_data["password"])

    def test_invalid_email(self):
        invalid_data = {
            "email": "invalid-email",
            "password": "SecurePassword123"
        }
        with self.assertRaises(ValueError):
            self.user_schema.load(invalid_data)

    def test_missing_password(self):
        invalid_data = {
            "email": "test@example.com"
        }
        with self.assertRaises(ValueError):
            self.user_schema.load(invalid_data)

    def test_short_password(self):
        invalid_data = {
            "email": "test@example.com",
            "password": "short"
        }
        with self.assertRaises(ValueError):
            self.user_schema.load(invalid_data)

if __name__ == '__main__':
    unittest.main()