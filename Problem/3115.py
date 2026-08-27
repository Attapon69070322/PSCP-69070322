"""ARCADE"""
first = input().split()
num = int(first[0])
m_list = []
total = []
for _ in range(num):
    o, c = map(int, input().split())
    m_list.append([o, c])

num1 = input().split()
for i in num1:
    TIME = int(i)
    count = 0
    for r in m_list:
        if r[0] <= TIME < r[1]:
            count += 1
    total.append(count)

print(*total)
