from django.test import TestCase
from django.test.client import Client
from django.test.utils import override_settings

class BasicTest(TestCase):
    def setUp(self):
        self.c = Client()

    def test_index(self):
        resp = self.c.get("/")
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "index.html")
        self.assertTemplateUsed(resp, "base.html")

    @override_settings(DEBUG=True)
    def test_static(self):
        resp = self.c.get("/static/style.css")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.content, "sss\n")

    @override_settings(DEBUG=True)
    def test_favicon(self):
        resp = self.c.get("/favicon.ico")
        self.assertEqual(resp.status_code, 200)

    def test_redirect(self):
        resp = self.c.get("/log", follow=True)
        self.assertEqual(
            resp.redirect_chain, [('http://testserver/log/', 302)]
        )
        self.assertTemplateUsed(resp, "log/index.html")

    def test_ajax(self):
        resp = self.c.get("/idxw")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.content, '{"message": "hello ajax"}')
        resp = self.c.get("/idxw?foo")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.content, '{"message": "hello ajax"}')
        resp = self.c.get("/idxw?asd=foo")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.content, '{"afoo": 1}')

