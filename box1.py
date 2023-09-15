"""Draw a square with sides of length n."""

def draw_square(n):
  square = ""
  i = 0
  while i < n:
    square += "*" * n
    i += 1
  return square
