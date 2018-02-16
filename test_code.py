#!/usr/bin/env python
import unittest
import number_calculator

class Test_Number_Calculator(unittest.TestCase):
  def test_get_average_of_four(self):
    input_argument  = [ 1, 2, 3, 4]
    expected_result = [2.5, 4]
    returned_result = number_calculator.calculator(input_argument)
    self.assertEquals(expected_result, returned_result)
    
