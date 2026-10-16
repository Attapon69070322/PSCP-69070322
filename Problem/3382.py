"""backward"""
k = []
while True:
    n = input()
    if n == "NULL":
        break
    k.append(n)

k.reverse()
for item in k:
    print(item)