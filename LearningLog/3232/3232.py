"""frog"""
n, n1 = map(int, input().split())
meter = 0
score = 0
for i in range(n):
    i += 1
    meter = meter + n
    n = n - 2
    score += 1
    if meter >= n1:
        break

if meter < n1:
    score = -1
    print(score)
else:
    print(score)
