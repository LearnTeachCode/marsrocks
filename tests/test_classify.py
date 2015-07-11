import unittest
from flask import url_for, request

from base import BaseTestCase
from project.models import User, Feature, Classification
from project import db, app
from testing_helpers import login


# these tests check that we get a 200 response code for all the routes
class TestClassify(BaseTestCase):

    #visitors get static template
    def test_visitors_see_classify_static(self):
        self.client.get(url_for('classify.index'))
        self.assert_template_used('classify_static.html')

    #logged in users get classify form
    def test_logged_in_users_see_classify(self):
        with self.client:
            login(self)
            self.client.get(url_for('classify.index'))
            self.assert_template_used('classify.html')

    # logged users can classify a photo
    def test_logged_in_users_can_classify_photo(self):
        user = db.session.query(User).first()
        feature1 = Feature.query.filter_by(slug='layered_rocks').first()
        feature2 = Feature.query.filter_by(slug='blueberries').first()

        with self.client:
            login(self)
            response = self.client.post(
                url_for('classify.index'),
                data = dict(
                    layered_rocks='y',
                    blueberries='y'
                    )
                )
            classify1 = Classification.query.filter_by(feature_id=feature1.id).first()
            classify2 = Classification.query.filter_by(feature_id=feature2.id).first()
            self.assertTrue(classify1.user_id == user.id)
            self.assertTrue(classify2.user_id == user.id)
            self.assertEqual(response.status_code, 302)

    # logged users must select at least one feature
    def test_logged_in_must_select_feature(self):
        user = db.session.query(User).first()
        feature = db.session.query(Feature).first()

        with self.client:
            login(self)
            response = self.client.post(
                url_for('classify.index')
                )
            classify = Classification.query.filter_by(user_id=user.id).first()
            self.assertTrue(classify == None)
            self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
