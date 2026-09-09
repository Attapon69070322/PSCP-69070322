"""FYFYFYYYYYILMNiLYT"""
n = int(float(input()) * 100)
n1 = int(input())
for i in range(n1):
    i += 1
    n += (n * 381) // 10000

print(f"{n//100}.{n%100:02d}")
