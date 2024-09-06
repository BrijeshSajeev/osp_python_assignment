#  Sort a list of tuples based on the second element.

# Sample input
lst = [(1, 2), (3, 1), (5, 6), (7, 8), (9, 0)]

# Sample output
print(sorted(lst, key=lambda x: x[1]))
