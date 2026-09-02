"""sanya"""

n = int(input())
for i in range(1 ,n+1):
    if not i % 5:
        print("X",end="")
    else:
        print("*",end="")
