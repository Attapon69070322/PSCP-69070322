"""แปลงดอกไม้"""
import math as m
l, n = map(int, input().split())
c = 1
f = 0
multiplier = 1
while c <= n:
    c += multiplier
    multiplier += 1
    f += 1
print(m.ceil(f / l))
