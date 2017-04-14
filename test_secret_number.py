# from __future__ import absolute_import

import unittest
from secret_number import get_numbers_list

class TestBinaryList(unittest.TestCase):

    def test_get_list_binaries_returns_correct_list(self):
        # arrange
        length = 3
        digit = -1
        expected_list = [1,3,5,7]

        # act
        numbers = get_numbers_list(number_length=length, digit=digit)

        # assert
        self.assertEqual(expected_list, numbers)