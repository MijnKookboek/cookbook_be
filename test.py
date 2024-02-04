import unittest

import requests


class TestClass(unittest.TestCase):
    def test_print_hello(self):
        self.assertEqual(requests.get('http://localhost:8080').text, 'hello world')
