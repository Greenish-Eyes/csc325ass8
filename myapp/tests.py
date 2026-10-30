from django.test import TestCase

# Create your tests here.

#add tests for home and about views
class SimpleTest(TestCase):
    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<h1>Hello, world!</h1>")

    def test_about(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<h1>About Page</h1>")