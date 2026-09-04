"""OHM"""
n = int(input())
n1 = int(input())
d = int(input())
status = "a"
spec = 0
total = n + n1
if d > 3:
    total = total + (total // 2)

if total >= 1500:
    status = "5"
elif total >= 1000:
    status = "4"
elif total >= 500:
    status = "3"
elif total >= 200:
    status = "2"
elif total < 200:
    status = "1"

if status == "5" and d >= 7:
    spec = 99
elif status == "4" and n1 > 300:
    spec = 88

print(total)
print(status)
print(spec)
