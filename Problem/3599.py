"""sumofnumber"""
n = int(input())
n1 = 0
while n > 0:
    num = int(input())
    if num == -1:
        break
    n1 += num
    if n1 == n:
        break

print(n1)
