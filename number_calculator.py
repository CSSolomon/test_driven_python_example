#!/usr/bin/env python
def calculator(input_argument):
  average = sum(input_argument) / len(input_argument)
  maximum = max(input_argument)
  return [average, maximum]
