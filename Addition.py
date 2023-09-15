def find_sum(n):
  """
  Find the sum of the first and last digits of a five-digit number.
  Returns: The sum of the first and last digits of n.
  """
  first_digit = n // 10000
  last_digit = n % 10
  return first_digit + last_digit
  
  N = int(input())
  print("The sum of the first and last digits of {}".format(N), "=", find_sum(N), sep=" ")
