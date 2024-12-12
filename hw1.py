import math

rad = float(input())
leng = 2 * math.pi * rad
ar = math.pi * rad ** 2
print(round(leng, 2), round(ar, 2))

x, y = 10, 55
print(x, y)
x, y = y, x
print(x, y)

import math

g = 9.81
l = float(input())
t = 2 * math.pi * math.sqrt(l/g)
print(round(t, 2))
