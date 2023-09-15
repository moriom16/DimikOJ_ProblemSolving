  """
  Check if a number is a perfect square.
  Returns:True if n is a perfect square, False otherwise.
  """
def is_perfect_square(n):
  sqrt = math.sqrt(n)
  return sqrt.is_integer()


N = int(input())
if is_perfect_square(N):
  print("YES")
else:
  print("NO")
