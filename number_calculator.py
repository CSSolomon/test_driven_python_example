#!/usr/bin/env python
def calculator(input_argument):
  if input_argument[0] < 0:
    are_negatives = True 
  else:
    are_negatives = False

  for number in input_argument:
    if number < 0:
      is_negative = True 
    else:
      is_negative = False
    if not is_negative == are_negatives:
      return None
  sorted_input_argument = sorted(input_argument)

  if sorted_input_argument[1] == sorted_input_argument[2] == sorted_input_argument[3]:
    return 3.0 * sorted_input_argument[1] / sorted_input_argument[0]
  elif sorted_input_argument[0] == sorted_input_argument[1] == sorted_input_argument[2]:
    return 3.0 * sorted_input_argument[0] / sorted_input_argument[3]
    

  average = 1.0 * sum(input_argument) / len(input_argument)
  maximum = 1.0 * max(input_argument)
  return [average, maximum]

def convert_string_to_list_of_numbers(input_string):
  return [1, 2, 3, 4]
