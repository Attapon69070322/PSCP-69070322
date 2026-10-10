"""calories"""
n1 = 0
while True:
    n = int(input())
    if n == 1:
        n1 += 100
    if n == 2:
        n1 += 120
    if n == 3:
        n1 += 200
    if n == 4:
        n1 += 60
    if n == 5:
        print("Bye Bye")
        break

print(f"Total Calories: {n1}")
