import unittest
from backend.app import app
from backend.database import db
from backend.models import User

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_signup(self):
        response = self.app.post('/signup', json={
            'email': 'test@example.com',
            'password': 'securepassword'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Success', response.data)

    def test_signup_duplicate(self):
        self.app.post('/signup', json={
            'email': 'test@example.com',
            'password': 'securepassword'
        })
        response = self.app.post('/signup', json={
            'email': 'test@example.com',
            'password': 'anotherpassword'
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'User already exists', response.data)

    def test_signin(self):
        self.app.post('/signup', json={
            'email': 'test@example.com',
            'password': 'securepassword'
        })
        response = self.app.post('/signin', json={
            'email': 'test@example.com',
            'password': 'securepassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login successful', response.data)

    def test_signin_invalid_credentials(self):
        response = self.app.post('/signin', json={
            'email': 'test@example.com',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 401)
        self.assertIn(b'Invalid credentials', response.data)

if __name__ == '__main__':
    unittest.main()