"""
Sort three numbers in increasing order.
    a: The first number || b: The second number || c: The third number.
Returns: The three numbers in increasing order.
"""
def sort_numbers(a, b, c):
  return sorted([a, b, c])

T = int(input())
for t in range(1, T + 1):
  a, b, c = map(int, input().split())
  a, b, c = sort_numbers(a, b, c)
  print("Case #{}: {}".format(t, " ".join([str(a), str(b), str(c)])))
