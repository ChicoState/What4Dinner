from django.test import TestCase

from API import API_data as api


class TestAPI(TestCase):
    '''
    Test suite to test the functionality of our API logic
    using varying permutations of search parameters
    '''

    def setUp(self) -> None:
        self.query = "chicken"
        self.num_of_ingredients = ""
        self.diet_type = ""
        self.health_type = ""
        self.meal_type = ""
        self.calories = ""
        self.time = ""
        return super().setUp()

    def test_single_parameter_search(self):
        '''Test API functionality only using the required "query" field'''
        ret = api.get_api_data(self.query, num_of_ingredients="",
                               diet_type="", health_type="", meal_type="", calories="", time="")
        self.assertEqual(ret.status_code, 200)

    def test_two_parameter_search(self):
        '''
        Test API functionality only using the required "query" field and 
        1 additional field.
        '''
        ret = api.get_api_data(self.query, self.num_of_ingredients,
                               diet_type="", health_type="", meal_type="", calories="", time="")
        self.assertEqual(ret.status_code, 200)

    def test_three_parameter_search(self):
        '''
        Test API functionality only using the required "query" field and 
        2 additional fields.
        '''
        ret = api.get_api_data(self.query, self.num_of_ingredients,
                               self.diet_type, health_type="", meal_type="", calories="", time="")
        self.assertEqual(ret.status_code, 200)

    def test_four_parameter_search(self):
        '''
        Test API functionality only using the required "query" field and 
        3 additional fields.
        '''
        ret = api.get_api_data(self.query, self.num_of_ingredients,
                               self.diet_type, self.health_type, meal_type="", calories="", time="")
        self.assertEqual(ret.status_code, 200)

    def test_five_parameter_search(self):
        '''
        Test API functionality only using the required "query" field and 
        4 additional fields.
        '''
        ret = api.get_api_data(self.query, self.num_of_ingredients,
                               self.diet_type, self.health_type,
                               self.meal_type, calories="", time="")
        self.assertEqual(ret.status_code, 200)

    def test_six_parameter_search(self):
        '''
        Test API functionality only using the required "query" field and 
        5 additional fields.
        '''
        ret = api.get_api_data(self.query, self.num_of_ingredients,
                               self.diet_type, self.health_type,
                               self.meal_type, self.calories, time="")
        self.assertEqual(ret.status_code, 200)

    def test_all_parameter_search(self):
        '''Test API functionality using all provided search fields'''
        ret = api.get_api_data(self.query,
                               self.num_of_ingredients,
                               self.diet_type,
                               self.health_type,
                               self.meal_type,
                               self.calories,
                               self.time)
        self.assertEqual(ret.status_code, 200)
