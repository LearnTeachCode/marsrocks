import unittest

from base import BaseTestCase

# these tests check that we get a 200 response code for all the routes
class BaseTest(BaseTestCase):

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about(self):
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)

    def test_stats(self):
        response = self.client.get('/stats')
        self.assertEqual(response.status_code, 200)

    def test_classify(self):
        response = self.client.get('/classify')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
