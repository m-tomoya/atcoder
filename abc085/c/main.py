import math
from collections import defaultdict

N, Y = map(int, input().split())
x = -1
y = -1
z = -1
for a in range(N+1):
    for b in range(N+1):
        c = N-(a+b)
        total = 10000*a + 5000*b + 1000*c
        if 0 <= c <= 2000 and total == Y:
            x = a
            y = b
            z = c
            print(x, y, z)
            exit()
        else:
            continue

print(x, y, z)
