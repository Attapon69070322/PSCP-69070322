"""coffee"""

n = int(input())
score = 0
table =[]
for i in range(n):
    i += 1
    am = int(input())
    score += am
    table.append(am)

print(score)
print(max(table))
print(min(table))
print(f"{score/n:.1f}")
