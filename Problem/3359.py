"""BOW"""
N = int(input())
COUNTS = {}
for _ in range(N):
    SIZE = int(input())
    if SIZE in COUNTS:
        COUNTS[SIZE] += 1
    else:
        COUNTS[SIZE] = 1

print(max(COUNTS.values()))
