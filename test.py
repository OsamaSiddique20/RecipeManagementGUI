# test_app.py
import unittest
from app import create_app
from extensions import db
from models.recipe import Recipe

class TestAppRoutes(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()

    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    # def test_search_route(self):
    #     response = self.app.get('/search?search=1')
    #     self.assertEqual(response.status_code, 200)

    # def test_add_recipe_route(self):
    #     response = self.app.get('/add-recipe')
    #     self.assertEqual(response.status_code, 200)

    # def test_update_recipe_route(self):
    #     response = self.app.get('/update-recipe/17')
    #     self.assertEqual(response.status_code, 200)

    # def test_delete_recipe_route(self):
    #     response = self.app.get('/delete/17')
    #     self.assertEqual(response.status_code, 200)

    def test_add_method(self):
        data={
                'name': "name",
                'instructions': "instructions",
                'ingredients': "ingredients,sahdg,sdasd",
                'category': "category",
                'rating': 3
            }
        try:
            Recipe.add(data)
            flag=False
        except:
            flag=True
        self.assertTrue(flag)



if __name__ == '__main__':
    unittest.main()