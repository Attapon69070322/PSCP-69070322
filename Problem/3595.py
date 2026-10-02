"""meteor"""
a = float(input())
b = int(input())
c = float(input())

dih = 0
m = 1

while a >= c:
    dih += m
    a /= b
    m *= b

print(dih)
