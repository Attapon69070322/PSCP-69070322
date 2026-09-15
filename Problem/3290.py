"""fifah"""
n = int(input())
n1 = int(input())
center = n1 // 2
for i in range(n1):
    print(" "*abs(i - center) + "*"*n)
