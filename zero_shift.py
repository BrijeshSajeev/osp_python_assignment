# Shift all zeros in a list towards right by maintaining the order of list.

def shift_zeros(lst):
    return [i for i in lst if i != 0] + [0] * lst.count(0)

# Sample input
lst = [0, 1, 0, 3, 2, 1, 2]
# lst = [0, 1, 0, 3, 2,100, 2000, 0, 0, 1, 2]
# lst = [8,0,0,7,6,5,2,1,0,0]

# Sample output
print(shift_zeros(lst))
