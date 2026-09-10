"""PASILYO"""
import math as ohm

n = input()
n = [int(d) for d in n]
total = ohm.prod(n)

if n[0] > 5:
    B = 9
elif n[1] > 5:
    B = 10
elif n[2] > 5:
    B = 11
elif n[3] > 5:
    B = 12
elif n[4] > 5:
    B = 14
else:
    B = 13

if n == n[::-1]:
    if n[0] + n[4] > 5:
        A = 1
    elif n[1] * n[3] > 5:
        A = 2
    else:
        A = 0
else:
    if n[4] and n[0] // n[4] > 5:
        A = 1
    elif n[1] - n[4] > 5:
        A = 2
    else:
        A = 0

if sum(n) > 25:
    C = 1
elif total > 55:
    C = 2
else:
    C = 0

print(str(B)+str(A)+str(C))
