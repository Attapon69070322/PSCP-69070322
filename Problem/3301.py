"""the box signature"""
w ,l ,s ,t = map(int, input().split())
ans = []
for i in range(s ,t+1):
    a = w % i
    b = l % i
    ans.append(a * b)
print(min(ans))
