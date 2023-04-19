'''
Test suite
'''
from django.test import TestCase

# Create your tests here.


class BasicTest(TestCase):
    '''
    Basic tests for the application
    '''

    def smoke_test_case(self):
        '''
        Smoke test case to ensure that test framework is working
        '''
        self.assertEqual(1, 1)
