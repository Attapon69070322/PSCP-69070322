"""castle"""
import math as m
n = int(input())
row = m.isqrt(n -1) + 1
p = n - (row - 1) ** 2

if p % 2 == 1:
    print(2 * row - 2)
else:
    print(2 * row - 3)
