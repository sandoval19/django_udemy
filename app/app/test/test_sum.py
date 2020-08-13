from django.test import TestCase
from app.sum import add,subtract

class SumTest(TestCase):

    def test_add_numbers(self):
        """Testing that two numbers are added together"""
        self.assertEqual(add(3,5),8)
    
    def test_subtract_numbers(self):
        """Test the substraction of two numbers"""
        self.assertEqual(subtract(5,11),6)