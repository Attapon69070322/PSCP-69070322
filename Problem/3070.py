"""ODD_EVEN"""
n1 = int(input())
n2 = int(input())
n3 = int(input())
e = 0
b = 0

if not n1 % 2:
    b += 1
else:
    e += 1

if not n2 % 2:
    b += 1
else:
    e += 1

if not n3 % 2:
    b += 1
else:
    e += 1

print(b)
print(e)
