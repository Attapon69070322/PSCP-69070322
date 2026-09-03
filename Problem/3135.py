"""Theif"""
n ,k ,t = map(int, input().split())
if t == 1:
    print(1)
else:
    m = 1
    p = 1
    while True:
        m = (m + k) % n
        if m == 1:
            break
        p += 1
        if m == t:
            break
    print(p)
