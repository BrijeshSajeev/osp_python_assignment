# Accept a list and print a tuple containing cubes of elements of L.

def cube_of_elements(L):
  return tuple(i**3 for i in L)

# Sample input
L = [1, 2, 3, 4, 5]

# Sample output
print(cube_of_elements(L)) # (1, 8, 27, 64, 125)
