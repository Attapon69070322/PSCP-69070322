"""taxi"""
k = int(input())
C = 0
if k == 1:
    C = 35
elif not k:
    C = 0
elif k <= 10:
    C = 35 + (k - 1) * 5
elif k > 10:
    C = 35 + (9 * 5) + (k - 10) * 8

print(C)
