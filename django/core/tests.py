from django.test import TestCase
from django.urls import reverse, resolve
from django.urls.exceptions import Resolver404

class UrlsTest(TestCase):
    def test_admin_url(self):
        """Проверяет, что маршрут /admin/ доступен и вызывает Django Admin."""
        url = reverse('admin:index')
        self.assertEqual(url, '/admin/')
        resolver = resolve('/admin/')
        self.assertEqual(resolver.view_name, 'admin:index')

    # def test_api_v1_url(self):
    #     """Проверяет, что маршрут /api/v1/ подключён через include."""
    #     try:
    #         resolver = resolve('/api/v1/')
    #         self.assertTrue(resolver.url_name is not None)
    #     except Resolver404:
    #         self.fail("Маршрут /api/v1/ не найден. Проверьте include('api.v1.urls').")