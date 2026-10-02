"""OLEANG"""
n = int(input())
n1 = []

for i in range(n):
    name,g,s,b = input().split( )
    g = int(g)
    s = int(s)
    b = int(b)
    total = g + s + b
    n1.append([name, g, s, b, total])
n1.sort(key=lambda x: (-x[1], -x[2], -x[3], x[0]))

row = 1
for i in range(n):
    if i > 0:
        if n1[i][1:4] != n1[i - 1][1:4]:
            row = i + 1
    name, g, s, b, total = n1[i]
    print(f"{row} {name} {g} {s} {b} {total}")
