'''
Views Test Suite
Testing can be ran using the following command
(assuming you are in an activated virtual environment):
./manage.py test API
'''
from unittest.mock import patch

from django.contrib.auth.models import User
from django.test import TestCase, override_settings
from django.urls import reverse
from django.contrib.auth import authenticate, login
from API.models import RecomendedRecipes, Profile
from API.form import SignUpForm, LoginForm

# TESTS MUST START WITH THE WORD TEST(EXAMPLE)
# def test_save_user_created_recipe(self):
#         '''Tests that a user created recipe is saved correctly'''
#         recipe = self.create_custom_recipe()
#         self.assertTrue(isinstance(recipe, CreateRecipe))

# Enable debug mode to show detailed error messages during tests


@override_settings(DEBUG=True)
class ViewTest(TestCase):
    '''Class for Views'''

    def setUp(self) -> None:
        '''Global setup to authenticate the user'''
        self.user = User.objects.create_user(
            username="Alex",
            password="Test",
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

    def test_recipe_details_no_objects(self):
        '''
        Test the recipe_details view when there are no recipe objects.
        '''
        url = reverse('recipes')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'API/recipes.html')
        self.assertQuerysetEqual(response.context['recipe_obj'], [])

class SignupTestCase(TestCase):
    '''Class for Sign Up Test Views'''
    def test_signup(self):
        '''Testing Sign Up Form and View'''
        form_data = {
            'first_name': 'Test',
            'last_name': 'User',
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword',
            # Include other required fields for the SignUpForm
        }
        
        form = SignUpForm(data=form_data)
        self.assertTrue(form.is_valid())
        
        response = self.client.post('/signup/', form_data)
        self.assertEqual(response.status_code, 302)
        
        user = User.objects.get(username='testuser')
        self.assertIsNotNone(user)
        
        profile = Profile.objects.get(user=user)
        self.assertIsNotNone(profile)