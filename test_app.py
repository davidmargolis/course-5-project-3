#!/usr/bin/env python3

import unittest

import app


class TestApp(unittest.TestCase):
    def test_home_page(self):
        with app.app.test_client() as test_client:
            response = test_client.get('/')
            assert response.status_code == 200
            assert b'Hello World!' in response.data


if __name__ == '__main__':
    unittest.main()
