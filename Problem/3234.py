"""SANTAKT"""
n ,n1 = input().split()
m = int(n1)

for i in range(m):
    i += 1
    if n == "R":
        print("Red", end=" ")
        n = "G"
    elif n == "G":
        print("Green", end=" ")
        n = "B"
    elif n == "B":
        print("Blue", end=" ")
        n = "R"
