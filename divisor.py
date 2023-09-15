  """
  Find all the factors of a number.
    n: The number to find the factors of.
  Returns: A list of all the factors of n.
  """
def factors(n):
  factors = []
  for i in range(1, n + 1):
    if n % i == 0:
      factors.append(i)
  return factors

T = int(input())
for t in range(1, T + 1):
  n = int(input())
  factors = factors(n)
  print("Case #{}: {}".format(t, " ".join([str(f) for f in factors])))
