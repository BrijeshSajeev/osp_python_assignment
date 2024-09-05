# Take two numbers N and K as input. Create a list L of length N and initialize it with zeros. Change the value to 1 of even indexes if k is even. Else change the value to 1 of odd indexes. 

N = int(input("Enter the value of N: "))
K = int(input("Enter the value of K: "))

L = [0] * N

if K % 2 == 0:
  for i in range(0, N, 2):
    L[i] = 1
else:
  for i in range(1, N, 2):
    L[i] = 1

print(L)
