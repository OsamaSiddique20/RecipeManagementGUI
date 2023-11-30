import unittest
from flask import Flask, url_for
from app import create_app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_index_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    # def test_search_route(self):
    #     response = self.client.get('/search?search=1')
    #     self.assertEqual(response.status_code, 200)

    # def test_nonexistent_recipe_search_route(self):
    #     response = self.client.get('/search?search=999')
    #     self.assertEqual(response.status_code, 200) 
 


if __name__ == '__main__':
    print(1111)
    unittest.main()
