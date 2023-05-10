'''
Model Test Suite
Testing can be ran using the following command 
(assuming you are in an activated virtual environment):
./manage.py test API
'''

from API.models import CreateRecipe, RecipeSearch, RecomendedRecipes
from django.contrib.auth.models import User
from django.test import TestCase


class ModelTest(TestCase):
    '''
    Tests model saving functionality for models found in models.py
    '''

    def setUp(self) -> None:
        '''Global setup to create a user account'''
        self.user = User.objects.create_user(
            username="Jake",
            password="test",
            email="test@test.com")
        self.client.force_login(user=self.user)
        super().setUp()

    def create_recipe_search(self):
        '''Creates a simple RecipeSearch object'''
        return RecipeSearch.objects.create(Recipe_Name="spaghetti")

    def create_custom_recipe(self):
        '''Simulates a user-created recipe'''
        return CreateRecipe.objects.create(Create_RecipeName="Test created recipe",
                                           Create_Ingrediants="123 ingrediants",
                                           Create_Meal_Type="Dinner",
                                           Create_Health_Type="DASH",
                                           Create_Diet="Balanced",
                                           Create_Calories="123000",
                                           Create_Time="45 minutes",
                                           Create_Instruct="1. bake 2. eat",
                                           Upload_Image="/ Users/jakewest/Desktop/profilePic.jpg")

    def test_models_smoke_test(self):
        '''smoke test'''
        self.assertEqual(1, 1)

    def test_save_recipe_search(self):
        '''Ensure that a users search is handled correctly'''
        recipe = self.create_recipe_search()
        self.assertTrue(isinstance(recipe, RecipeSearch))

    def test_save_user_created_recipe(self):
        '''Tests that a user created recipe is saved correctly'''
        recipe = self.create_custom_recipe()
        self.assertTrue(isinstance(recipe, CreateRecipe))

    def test_save_user_profile(self):
        '''Tests that a users bio and profile picture are updated correctly'''
        pass
