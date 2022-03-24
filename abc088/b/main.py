import math
from collections import defaultdict

N = int(input())
x = list(map(int, input().split()))

x.sort()

a = 0
b = 0

for i in range(N):
    if i % 2 == 0:
        a += x[i]
    else:
        b += x[i]

dif = abs(a-b)
print(dif)
