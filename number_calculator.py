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

  average = 1.0 * sum(input_argument) / len(input_argument)
  maximum = 1.0 * max(input_argument)
  return [average, maximum]
