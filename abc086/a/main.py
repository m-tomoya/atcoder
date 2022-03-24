import math
from collections import defaultdict


s = input().split()
total = int(s[0])*int(s[1])
if total % 2 == 0:
    print("Even")
else:
    print("Odd")
