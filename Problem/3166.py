"""CHALEER"""
n = int(input())
pas = "PASS"
score = 0
for i in range(n):
    i += 1
    n1 = int(input())
    score += n1
    if n1 < 50:
        pas = "FAIL"

avg = score / n
if avg < 60:
    pas = "FAIL"

print(f"{avg:.1f}")
print(pas)
