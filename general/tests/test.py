from django.test import TestCase


class GeneralEndPointsTest(TestCase):

    def test_home_view(self):
        response = self.client.get('', format='json')
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):
        response = self.client.get('/login/', format='json')
        self.assertEqual(response.status_code, 200)

    def test_register_view(self):
        response = self.client.get('/register/', format='json')
        self.assertEqual(response.status_code, 200)

