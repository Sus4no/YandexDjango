from django.test import TestCase, Client


class StaticUrlTests(TestCase):
    def test_catalog_endpoint(self):
        response = Client().get('/catalog/')
        self.assertEqual(response.status_code, 200)

        response = Client().get('/catalog/123/')
        self.assertEqual(response.status_code, 200)

        response = Client().get('catalog/abc/')
        self.assertEqual(response.status_code, 404)
