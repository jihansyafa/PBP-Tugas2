from django.test import TestCase, Client

# Create your tests here.
class URLTests(TestCase):
    def test_json(self):
        response = self.client.get('/mywatchlist/json/')
        self.assertEqual(response.status_code, 200)
    
    def test_xml(self):
        response = self.client.get('/mywatchlist/xml/')
        self.assertEqual(response.status_code, 200)

    def test_html(self):
        response = self.client.get('/mywatchlist/html/')
        self.assertEqual(response.status_code, 200)