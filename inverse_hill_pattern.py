# Print the following inverse hill pattern

def inverse_hill_pattern(n):
  for i in range(n, 0, -1):
    print(" " * (n - i), end="")
    print("*" * (2 * i - 1))

n = 3
inverse_hill_pattern(n)
