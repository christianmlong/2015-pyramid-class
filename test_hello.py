import unittest

class HelloWorldUnitTests(unittest.TestCase):
    def test_hello_world(self):
        from hello import hello_world
        result = hello_world({})
        self.assertEqual(result.body, b'Hello world!')

if __name__ == '__main__':
    unittest.main()
