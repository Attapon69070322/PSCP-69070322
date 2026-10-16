"""Dupe"""
m = int(input())
n = int(input())

group1 = set()
for _ in range(m):
    group1.add(input().strip())

group2 = set()
for _ in range(n):
    group2.add(input().strip())

duplicates = group1.intersection(group2)

if not duplicates:
    print("Nope")
else:
    sorted_duplicates = sorted(duplicates, key=int, reverse=True)
    for student_id in sorted_duplicates:
        print(student_id)
