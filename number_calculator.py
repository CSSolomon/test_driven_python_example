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
  result = input_string.split()
  for index, number in enumerate(result):
    result[index] = float(number)
  return result

def get_input():
  return raw_input("Please give a list of four numbers, separated by spaces: ")

def main():
  value_string = get_input()
  value_list = convert_string_to_list_of_numbers(value_string)
  result = calculator(value_list)
  print result
  return result

if __name__ == "__main__":
  main()
