#!/usr/bin/env python
import unittest
import mock
import number_calculator
import sys

class Test_Number_Calculator(unittest.TestCase):
  def setUp(self):
    self.stdout = sys.stdout
    self.fd = open("/dev/null", "w")
    sys.stdout = self.fd

  def tearDown(self):
    sys.stdout = self.stdout
    self.fd.close()

  def test_get_average_of_four(self):
    input_argument  = [ 1, 2, 3, 4]
    expected_result = [2.5, 4]
    returned_result = number_calculator.calculator(input_argument)
    self.assertEquals(expected_result, returned_result)

  def test_get_average_of_four_second_list(self):
    input_argument  = [ 2, 4, 6, 8]
    expected_result = [5, 8]
    returned_result = number_calculator.calculator(input_argument)
    self.assertEquals(expected_result, returned_result)

  def test_with_negatives(self):
    input_argument  = [ -2, -4, -6, -8]
    expected_result = [-5, -2]
    returned_result = number_calculator.calculator(input_argument)
    self.assertEquals(expected_result, returned_result)

  def test_one_negative(self):
    input_argument  = [ 2, 4, -6, 8]
    expected_result = None
    returned_result = number_calculator.calculator(input_argument)
    self.assertEquals(expected_result, returned_result)

  def test_two_negatives(self):
    input_argument  = [ 2, -4, -6, 8]
    expected_result = None
    returned_result = number_calculator.calculator(input_argument)
    self.assertEquals(expected_result, returned_result)

  def test_three_equals(self):
    input_argument  = [ 3, 3, 3, 1]
    expected_result = 9
    returned_result = number_calculator.calculator(input_argument)
    self.assertEquals(expected_result, returned_result)

  def test_three_equals_second_list(self):
    input_argument  = [ 3, 3, 3, 9]
    expected_result = 1
    returned_result = number_calculator.calculator(input_argument)
    self.assertEquals(expected_result, returned_result)
    
  def test_three_equals_zero_smallest(self):
    input_argument  = [ 3, 3, 3, 0]
    with self.assertRaises(ZeroDivisionError):
      returned_result = number_calculator.calculator(input_argument)

  def test_input_string_to_number_list(self):
    input_argument  = "1 2 3 4"
    expected_result = [1, 2, 3, 4]
    returned_result = number_calculator.convert_string_to_list_of_numbers(
        input_argument)
    self.assertEquals(expected_result, returned_result)
    
  def test_input_string_to_number_list_two(self):
    input_argument  = "2 3 4 5"
    expected_result = [ 2, 3, 4, 5]
    returned_result = number_calculator.convert_string_to_list_of_numbers(
        input_argument)
    self.assertEquals(expected_result, returned_result)

  def test_input_string_to_number_list_invalid_list(self):
    input_argument  = "2 a 4 5"
    with self.assertRaises(ValueError):
      returned_result = number_calculator.convert_string_to_list_of_numbers(
          input_argument)

  def test_input_string_to_number_list_invalid_list(self):
    input_argument  = "2 a 4 5"
    with self.assertRaises(ValueError):
      returned_result = number_calculator.convert_string_to_list_of_numbers(
          input_argument)

  def test_give_mock_input(self):
    input_argument  = "2 3 6 5"
    expected_result = [4, 6]
    mock_object = mock.Mock(return_value = input_argument)
    with mock.patch("number_calculator.get_input", mock_object):
      returned_result = number_calculator.main()

    self.assertEquals(expected_result, returned_result)

  def test_shorter_list_one_value(self):
    input_argument  = [ 1 ]
    with self.assertRaises(ValueError):
      returned_result = number_calculator.calculator(input_argument)

  def test_shorter_list_two_values(self):
    input_argument  = [ 1 , 2]
    with self.assertRaises(ValueError):
      returned_result = number_calculator.calculator(input_argument)

  def test_longer_list_five_values(self):
    input_argument  = [ 1 , 2, 3, 4, 5]
    with self.assertRaises(ValueError):
      returned_result = number_calculator.calculator(input_argument)

unittest.main()
