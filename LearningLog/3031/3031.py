"""ink"""
import math as b
s ,n = map(int, input().split())
P = 3.1416
for i in range(n):
    i += 1
    x ,y = map(float, input().split())
    time = (P * (x**2 + y**2)) / s
    print(b.ceil(time))
