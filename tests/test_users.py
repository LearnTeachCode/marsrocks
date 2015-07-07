import unittest
from flask import request, url_for
from flask.ext.login import current_user

from base import BaseTestCase
from project import bcrypt
from project.models import User

class TestUserLogin(BaseTestCase):
    # ensure user can register
    def test_user_registration(self):
         with self.client:
            response = self.client.post(
                url_for('users.register'),
                data=dict(username="blahblah",
                          password="password",
                          confirm="password"),
                follow_redirects=True
                )
            self.assertEqual(response.status_code, 200)
            user = User.query.filter_by(username='blahblah').first()
            self.assertTrue(str(user) == '<name - blahblah>')

    # Ensure errors are thrown during an incorrect user registration
    def test_incorrect_user_registeration(self):
        with self.client:
            response = self.client.post('/register', data=dict(
                name='',
                password='python', confirm='python'
            ), follow_redirects=True)
            self.assertIn(b'This field is required.', response.data)
            self.assertIn(b'/register', request.url)

    # Ensure id is correct for the current/logged in user
    # def test_get_by_id(self):
    #     with self.client:
    #         response = self.client.post(
    #             url_for('users.login'),
    #             data=dict(username="admin", password="password"),
    #             follow_redirects=True
    #             )
    #         self.assertTrue(current_user.id == 1)
    #         self.assertFalse(current_user.id == 20)

    # Ensure given password is correct after unhashing
    def test_check_password(self):
        user = User.query.filter_by(username='admin').first()
        self.assertTrue(bcrypt.check_password_hash(user.password, 'password'))
        self.assertFalse(bcrypt.check_password_hash(user.password, 'foobar'))

    # Ensure that login behaves correctly for correct credentials
    def test_login_correct_credentials(self):
        with self.client:
            response = self.client.post(
                url_for('users.login'),
                data=dict(username="admin", password="password"),
                follow_redirects=True
                )
            # current_user is from flask-login
            self.assertTrue(current_user.username == 'admin')
            self.assertTrue(current_user.is_active())

    # Ensure that login behaves correctly for incorrect credentials
    def test_login_incorrect_credentials(self):
        with self.client:
            response = self.client.post(
                url_for('users.login'),
                data=dict(username="blah", password="blah"),
                follow_redirects=True
                )
            self.assertIn('Invalid credentials', response.data)
            self.assertFalse(current_user.is_active())

     # ensure logout redirect
    def test_logout_redirect(self):
        with self.client:
            self.client.post(
                url_for('users.login'),
                data=dict(user="admin", password="password"),
                follow_redirects=True
                )
            response = self.client.get(
                url_for('users.logout'),
                follow_redirects=True
                )
            self.assertEqual(response.status_code, 200)
            self.assertFalse(current_user.is_active())

    # ensure logout requires login
    def test_logout_route_requires_login(self):
        response = self.client.get(
            url_for('users.logout'),
            follow_redirects=False
            )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login?next=%2Flogout')


if __name__ == '__main__':
    unittest.main()
