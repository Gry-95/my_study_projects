from django.test import TestCase
from . import views


# Create your tests here.
class TestHoroscope(TestCase):

    def test_index(self):
        response = self.client.get('/horoscope/')
        self.assertEqual(response.status_code, 200)

    def test_libra(self):
        response = self.client.get('/horoscope/libra')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября)',
                      response.content.decode())

    def test_signs(self):
        for test_url, test_text in views.ZODIAC.items():
            response = self.client.get(f'/horoscope/{test_url}')
            self.assertIn(test_text, response.content.decode())

    def test_libra_redirect(self):
        for num, test_url in enumerate(views.ZODIAC):
            response = self.client.get(f'/horoscope/{num + 1}')
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.url, f'/horoscope/{test_url}')
