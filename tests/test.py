from unittest import TestCase
from main import prime_number

class TestPrimeNumber(TestCase):
   def test_is_prime(self):
      self.assertEqual(prime_number(7), 'prime')