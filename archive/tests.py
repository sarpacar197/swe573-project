from django.contrib.auth import get_user_model
from django.test import TestCase


class UserModelTests(TestCase):
    def test_custom_user_is_used(self):
        self.assertEqual(get_user_model()._meta.label, 'archive.User')

    def test_create_user_with_bio_and_region(self):
        user = get_user_model().objects.create_user(
            username='ayse', password='testpass123', bio='Weaver', region='Uşak'
        )
        self.assertEqual(user.region, 'Uşak')
        self.assertTrue(user.check_password('testpass123'))
