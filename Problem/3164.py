"""IMAX"""

n = int(input())
kai = []
for i in range(n):
    i += 1
    n1 = int(input())
    n2 = int(input())
    if n1 >= n2:
        kai.append(n1)
    else:
        kai.append(n2)

if n > 1:
    total = sum(kai)
    print(*kai ,sep=" + ", end=" = ")
    print(total)
elif n == 1:
    print(max(kai))
