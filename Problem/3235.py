"""FAT Rabbit"""
n = int(input())
w = 0
m_w = 0
name = ""
for i in range(n):
    i += 1
    rabbit, n1 = input().split()
    n1 = int(n1)
    if n1 > 15:
        w += 1
    if n1 > m_w:
        m_w = n1
        name = rabbit

print(w)
print(name)
