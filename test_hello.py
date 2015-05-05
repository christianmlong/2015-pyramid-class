import unittest

class HelloWorldUnitTests(unittest.TestCase):
    def test_hello_world(self):
        from hello import hello_world
        result = hello_world({})
        self.assertEqual(result.body, b'Hello world!')

class HelloWorldFunctionalTests(unittest.TestCase):
    def setUp(self):
        from hello import main
        app = main()
        from webtest import TestApp
        self.testapp = TestApp(app)

    def test_without_slash(self):
        res = self.testapp.get('/hello', status=200)
        self.assertTrue(b'Hello world!' in res.body)

    def test_with_slash(self):
        res = self.testapp.get('/hello/', status=200)
        self.assertTrue(b'Hello world!' in res.body)
