import math
from collections import defaultdict

N = int(input())
A = []
for _ in range(N):
    A.append(int(input()))
A.sort()

count = 0
mochi = 0
for i in range(N):
    if A[i] > mochi:
        count += 1
    mochi = A[i]

print(count)
