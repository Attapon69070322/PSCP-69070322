"""PRIME"""
x , y = map(int, input().split())
prime =[2, 3, 5, 7]
h = []
for i in range(x ,y+1):
    if i in prime:
        h.append(i)
    if i % 2 and i % 3 and i % 5 and i % 7 and i != 1:
        h.append(i)

if len(h) >= 1:
    print(*h)
print(f"Total primes: {len(h)}")
