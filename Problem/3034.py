"""mort"""
p ,r = map(int, input().split())
l = []
l1 = []
a = 0
for i in range(p):
    i += 1
    n = int(input())
    if n > r:
        a = a+1
    else:
        l.append(n)

for d in range(r):
    d += 1
    count_num = l.count(d)
    l1.append(count_num)

for j in range(r):
    A = l1[j]
    a += A - min(l1)

print(a)
