import unittest
from flask import url_for

from base import BaseTestCase

# these tests check that we get a 200 response code for all the routes
class BaseTest(BaseTestCase):
    def test_index(self):
        response = self.client.get(url_for('home.index'))
        self.assertEqual(response.status_code, 200)
        self.assert_template_used('index.html')

    def test_about(self):
        response = self.client.get(url_for('about.index'))
        self.assertEqual(response.status_code, 200)

    def test_stats(self):
        response = self.client.get(url_for('stats.index'))
        self.assertEqual(response.status_code, 200)

    def test_classify(self):
        response = self.client.get(url_for('classify.index'))
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.client.get(url_for('users.login'))
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        response = self.client.get(url_for('users.register'))
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
