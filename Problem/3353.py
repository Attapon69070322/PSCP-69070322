"""GMMPGMMT"""
n = list(map(int, input().split()))
k = 0
for i in reversed(n):
    if not i % 3 or not i % 5:
        k += 1
        print(i)

if not k:
    print("Nope")
