# Take two integers a and b and print all composite numbers between a and b. (Both a and b are inclusive)
def is_composite(num):
  if num < 4:
      return False
  for i in range(2, int(num ** 0.5) + 1):
      if num % i == 0:
          return True
  return False

def print_composite_numbers(a, b):
  composites = [i for i in range(a, b+1) if is_composite(i)]
  return composites

# Sample input
a, b = 1, 8

# Sample output
print(print_composite_numbers(a, b))
