#!/usr/bin/env python
def calculator(input_argument):
  average = 1.0 * sum(input_argument) / len(input_argument)
  maximum = 1.0 * max(input_argument)
  return [average, maximum]
