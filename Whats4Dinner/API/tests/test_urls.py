'''
URL Test Suite

Tests URL availability and non-data producing/consuming view rendering.

Testing can be ran using the following command 
(assuming you are in an activated virtual environment):
./manage.py test API
'''

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

# Create your tests here.


class UrlTestUnauthenticated(TestCase):
    '''
    Testing application URL's to ensure that they behave correctly
    when the user is NOT authenticated
    '''

    def test_url_smoke_test(self):
        """Smoke test"""
        self.assertEqual(1, 1)

    # Testing Endpoints

    def test_url_exists_at_correct_location_test_home_url(self):
        """Test access to the root url"""
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_test_about_url(self):
        """Test access to the root url"""
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_test_search_url(self):
        """Test access to the search url"""
        response = self.client.get(reverse("search"))
        self.assertEqual(response.status_code, 302)

    def test_url_exists_at_correct_location_test_signup_url(self):
        """Test access to the signup url"""
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_test_login_url(self):
        """Test access to the login url"""
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_test_userprofile_url(self):
        """Test access to the userprofile url"""
        response = self.client.get(reverse("userProfile"))
        self.assertEqual(response.status_code, 302)

    def test_url_exists_at_correct_location_test_editprofile_url(self):
        """Test access to the editprofile url"""
        response = self.client.get(reverse("editProfile"))
        self.assertEqual(response.status_code, 302)

    def test_url_exists_at_correct_location_test_profile_url(self):
        """Test access to the profile url"""
        response = self.client.get(reverse("profile"))
        self.assertEqual(response.status_code, 302)

    def test_url_exists_at_correct_location_test_logout_url(self):
        """Test access to the logout url"""
        response = self.client.get(reverse("logout"))
        self.assertEqual(response.status_code, 302)

    # Test that correct templates are used for each endpoint

    def test_home_template_name_correct(self):
        """Testing that the correct template is used on root url"""
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "API/home.html")

    def test_about_template_name_correct(self):
        """Testing that the correct template is used on about url"""
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "API/about.html")

    def test_signup_template_name_correct(self):
        """Testing that the correct template is used on signup url"""
        response = self.client.get(reverse("signup"))
        self.assertTemplateUsed(response, "API/signup.html")

    def test_search_template_redirect_for_unauthenticated_user(self):
        """Testing that the login template is used when user tries to 
        search but is not authenticated"""
        response = self.client.get(reverse("search"))
        self.assertTemplateNotUsed(response, "API/search.html")

    def test_userprofile_redirect_for_unauthenticated_user(self):
        """
        Testing that the login template is used when user tries to
        access the profile page but is not authenticated
        """
        response = self.client.get(reverse("userProfile"))
        self.assertTemplateNotUsed(response, "API/userprofile.html")

    def test_editprofile_redirect_for_unauthenticated_user(self):
        """
        Testign that the login template is used when user tries to
        access the edit profile page but is not authenticated
        """
        response = self.client.get(reverse("editProfile"))
        self.assertTemplateNotUsed(response, "API/editProfile.html")


class UrlTestAuthenticated(TestCase):
    '''
        Testing application URL's to ensure that they behave correctly
        when the user is authenticated
    '''

    def setUp(self) -> None:
        '''Global setup to authenticate the user'''
        self.user = User.objects.create_user(
            username="Jake",
            password="test",
            email="test@test.com"
        )
        self.client.force_login(user=self.user)
        super().setUp()

    def test_url_exists_at_correct_location_test_home_url(self):
        """Test access to the root url"""
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_test_about_url(self):
        """Test access to the root url"""
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_test_search_url(self):
        """Test access to the search url"""
        response = self.client.get(reverse("search"))
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_test_signup_url(self):
        """Test access to the signup url"""
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_test_login_url(self):
        """Test access to the login url"""
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_test_userprofile_url(self):
        """Test access to the userprofile url"""
        response = self.client.get(reverse("userProfile"))
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_test_editprofile_url(self):
        """Test access to the editprofile url"""
        response = self.client.get(reverse("editProfile"))
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_test_profile_url(self):
        """Test access to the profile url"""
        response = self.client.get(reverse("profile"))
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_test_logout_url(self):
        """Test access to the logout url"""
        response = self.client.get(reverse("logout"))
        self.assertEqual(response.status_code, 302)

    # Test that correct templates are used for each endpoint

    def test_home_template_name_correct(self):
        """Testing that the correct template is used on root url"""
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "API/home.html")

    def test_about_template_name_correct(self):
        """Testing that the correct template is used on about url"""
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "API/about.html")

    def test_search_template_name_correct(self):
        """Testing that the correct template is used on search url"""
        response = self.client.get(reverse("search"))
        self.assertTemplateUsed(response, "API/search.html")

    def test_signup_template_name_correct(self):
        """Testing that the correct template is used on signup url"""
        response = self.client.get(reverse("signup"))
        self.assertTemplateUsed(response, "API/signup.html")

    def test_userprofile_template_name_correct(self):
        """
        Testing that the login template is used when user tries to
        access the profile page and is authenticated
        """
        response = self.client.get(reverse("userProfile"))
        self.assertTemplateUsed(response, "API/userprofile.html")

    def test_editprofile_redirect_for_unauthenticated_user(self):
        """
        Testign that the login template is used when user tries to
        access the edit profile and is authenticated
        """
        response = self.client.get(reverse("editProfile"))
        self.assertTemplateUsed(response, "API/editProfile.html")
