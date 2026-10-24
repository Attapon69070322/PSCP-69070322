"""SPEEDINEEDTHIS"""
n = int(input())
result_map = {True:"YES",False:"NO"}

if n <= 1:
    prime = False
elif n == 2:
    prime = True
elif not n % 2 :
    prime = False
else:
    prime = True
    limit = int(n**0.5)
    for i in range(3, limit + 1, 2):
        if not n % i :
            prime = False
            break

print(result_map[prime])
