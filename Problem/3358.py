"""Chic"""
n = int(input())
weights = list(map(int, input().split()))

max_weights = []

for i in range(0, 2 * n, 2):
    w1 = weights[i]
    w2 = weights[i + 1]
    max_weights.append(max(w1, w2))

if n == 1:
    print(max_weights[0])
else:
    E = " + ".join(map(str, max_weights))
    total = sum(max_weights)
    print(f"{E} = {total}")
