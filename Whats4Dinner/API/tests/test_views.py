'''
Views Test Suite
Testing can be ran using the following command
(assuming you are in an activated virtual environment):
./manage.py test API
'''

from django.contrib.auth.models import User
from django.db import transaction
from django.test import TestCase, TransactionTestCase, Client, override_settings
from django.urls import reverse
from API.models import RecomendedRecipes, CreateRecipe

# TESTS MUST START WITH THE WORD TEST(EXAMPLE)
# def test_save_user_created_recipe(self):
#         '''Tests that a user created recipe is saved correctly'''
#         recipe = self.create_custom_recipe()
#         self.assertTrue(isinstance(recipe, CreateRecipe))

from unittest.mock import patch
from django.urls import reverse
from django.test import TestCase
from API.models import RecomendedRecipes


# Enable debug mode to show detailed error messages during tests
@override_settings(DEBUG=True)
class ViewTest(TestCase):
    '''Class for Views'''

    def setUp(self) -> None:
        '''Global setup to authenticate the user'''
        self.user = User.objects.create_user(
            username="Jake",
            password="test",
            email="test@test.com"
        )
        self.client.force_login(user=self.user)
        super().setUp()

    @classmethod
    def setUpTestData(cls):
        '''Setup Recomended Recipe Test Data'''
        # Create a recommended recipe for testing purposes
        cls.recipe = RecomendedRecipes.objects.create(Rec_Recipe_Name='Air Fryer Tilapia',
                                                      Rec_URL='https://www.allrecipes.com/recipe/8532964/air-fryer-tilapia/')

    def test_home_view_with_recipe(self):
        '''Test with a recomended recipe object'''
        # Patch the random.choice function to always return the test recipe
        with patch('API.views.random.choice', return_value=self.recipe):
            # Issue a GET request to the home page URL
            response = self.client.get(reverse('home'))

            # Check that the response status code is 200 OK
            self.assertEqual(response.status_code, 200)

            # Check that the correct template was used to render the response
            self.assertTemplateUsed(response, 'API/home.html')

            # Check that the recipe object is passed to the template context
            self.assertEqual(response.context['recipe'], self.recipe)

    def test_home_view_without_recipe(self):
        '''Test without Recomended Recipe Object'''
        RecomendedRecipes.objects.all().delete()
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'API/home.html')
        self.assertIsNone(response.context.get('recipe'))
        self.assertEqual(response.context.get('message'),
                         'There are no recipes to display.')

    def test_create_view_without_post(self):
        '''Checkin if the create view will show up with no post data'''
        response = self.client.get(reverse('create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'API/create.html')
        self.assertFalse(response.context['form'].is_bound)

    # def test_create_recipe_success(self):
    #     '''Creating a Recipe Test'''
    #     data = {
    #         'Create_RecipeName': 'Test Recipe',
    #         'Create_Ingrediants': 'Test Ingredient 1, Test Ingredient 2',
    #         'Create_Meal_Type': 'Breakfast',
    #         'Create_Health_Type': 'Healthy',
    #         'Create_Diet': 'Vegan',
    #         'Create_Calories': '200',
    #         'Create_Time': '30 minutes',
    #         'Create_Instruct': 'Test Instructions',
    #         'Upload_Image': r'C:\Users\alexr\OneDrive\Desktop\Whats4Dinner\What4Dinner\Whats4Dinner\static\Alex.jpg',
    #         "message": "Recipe created successfully!",
    #     }
    #     url = reverse('create')
    #     response = self.client.post(url, data)
    #     self.assertEqual(response.status_code, 200)

    #     # Check if the recipe is created
    #     recipe_exists = CreateRecipe.objects.filter(
    #         Create_RecipeName='Test Recipe').exists()
    #     self.assertTrue(recipe_exists, "Recipe was not created")

    #     # Get the created recipe
    #     created_recipe = CreateRecipe.objects.get(Create_RecipeName='Test Recipe')
    #     self.assertEqual(created_recipe.Create_Ingrediants, 'Test Ingredient 1, Test Ingredient 2')
    #     # Add more assertions for other fields as needed

    #     # Assert the filtered queryset against an expected value for detailed failure output
    #     expected_queryset = [created_recipe]
    #     self.assertQuerysetEqual(
    #         CreateRecipe.objects.filter(Create_RecipeName='Test Recipe'),
    #         expected_queryset,
    #         transform=lambda x: x,
    #         ordered=False,
    #         msg="The filtered queryset does not match the expected queryset."
    #     )

        # self.assertContains(response, 'Recipe created successfully!')

    def test_recipe_details_no_objects(self):
        '''
        Test the recipe_details view when there are no recipe objects.
        '''
        url = reverse('recipes')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'API/recipes.html')
        self.assertQuerysetEqual(response.context['recipe_obj'], [])

    # def test_recipe_details_with_objects(self):
    #     '''
    #     Test the recipe_details view when there are recipe objects.
    #     '''
    #     # Create recipe objects for testing
    #     recipe1 = CreateRecipe.objects.create(Create_RecipeName='Recipe 1')
    #     recipe2 = CreateRecipe.objects.create(Create_RecipeName='Recipe 2')

    #     url = reverse('recipes')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'API/recipes.html')
    #     self.assertQuerysetEqual(
    #         response.context['recipe_obj'],
    #         [repr(recipe1), repr(recipe2)],
    #         ordered=False
    #     )