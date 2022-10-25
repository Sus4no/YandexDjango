from django.test import TestCase, Client


class StaticUrlTests(TestCase):
    args = {
        '': 200,
        '123/': 200,
        '65/': 200,
        'abc/': 404,
        'a.s71/': 404,
        '-149/': 404,
        '-pqoi/': 404,
        '12.751/': 404,
        '.112/': 404,
    }

    def test_catalog_endpoint(self):
        for i in self.args.keys():
            response = Client().get('/catalog/{}'.format(i))
            self.assertEqual(response.status_code, self.args[i])
