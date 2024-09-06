# 10. Given n indicating number of rows, print a right angled triangle of squares of numbers with n rows.
#  Example
# Input   3
# Output  
#   1
#   2    4
#   3    9    81


def print_triangle_of_squares(n):
    for num in range(1, n+1):
        value = num
        for j in range(num):
            print(value, end=" ")
            value **= 2  # Square the current value
        print()

# Sample input
n = 3

# Sample output
print_triangle_of_squares(n)
