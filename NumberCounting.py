"""
  Count the number of numbers in a line.
  Returns: The number of numbers in line.
  """
def count_numbers(line):
  numbers = line.split()
  return len(numbers)


T = int(input())
for _ in range(T):
  line = input()
  print(count_numbers(line))
