# import numpy as np
# points = list(map(int, input().split()))
# a = np.array([points[0], points[1]])
# b = np.array([points[2], points[3]])
# distance = np.linalg.norm(a-b)
# print(distance)

import math
a, b, c, d = map(float, input(), split())
print(math.hypot(c-a, d-b))
