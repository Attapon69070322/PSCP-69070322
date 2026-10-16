"""pls speed"""
n, s = map(int, input().split())

next_person = [0] * (n + 1)
for i in range(1, n + 1):
    next_person[i] = int(input())

visited = set()
curr = s

while curr  and curr not in visited:
    visited.add(curr)
    curr = next_person[curr]

print(len(visited))
