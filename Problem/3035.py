"""Tiktok tiktok tiktok tiktok"""
r ,x ,y = map(int, input().split())
X = x ** 2
R = r ** 2
Y = y ** 2
xy = X + Y
if xy < R :
    print("IN")
elif xy == R :
    print("ON")
elif xy > R :
    print("OUT")
