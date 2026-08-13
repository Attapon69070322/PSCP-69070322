"""liam"""
x1 ,y1 ,w1 ,h1 = map(int, input().split())
x2 ,y2 ,w2 ,h2 = map(int, input().split())
r1 = x1 + w1
t1 = y1 + h1
r2 = x2 + w2
t2 = y2 + h2

warp = min(r2, r1) - max(x1, x2)
harp = min(t1, t2) - max(y1, y2)
if harp > 0 and warp > 0:
    a = harp * warp
    print(a)
else:
    print("no overlapping")
