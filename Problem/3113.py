"""RABBIT_RAMEN"""
s, t = map(str, input().split())
above = input()
f = above[0]
much = 0
n = 0
if len(above) > 1:
    n = int(above[2::1])
if s == "S" and t == "R":
    much += 60
    if f == "P":
        much += 15 * n
    elif f == "E":
        much += 10 * n
    elif f == "N":
        much += 0
elif s == "S" and t == "T":
    much += 80
    if f == "P":
        much += 15 * n
    elif f == "E":
        much += 10 * n
    elif f == "N":
        much += 0
elif s == "M" and t == "R":
    much += 80
    if f == "P":
        much += 15 * n
    elif f == "E":
        much += 10 * n
    elif f == "N":
        much += 0
elif s == "M" and t == "T":
    much += 100
    if f == "P":
        much += 15 * n
    elif f == "E":
        much += 10 * n
    elif f == "N":
        much += 0
elif s == "L" and t == "R":
    much += 100
    if f == "P":
        much += 15 * n
    elif f == "E":
        much += 10 * n
    elif f == "N":
        much += 0
elif s == "L" and t == "T":
    much += 120
    if f == "P":
        much += 15 * n
    elif f == "E":
        much += 10 * n
    elif f == "N":
        much += 0

print(much)
