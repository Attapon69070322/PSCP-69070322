"""bonus"""
H, AGE, MONEY = input().split()
A = int(AGE)
M = int(MONEY)
po = M / 100
total = 0

if H == "M":
    total += 1500
    if A <= 5:
        total += po * 6
    elif A <= 10:
        total += po * 8
    else:
        total += po * 10

elif H == "B":
    total += 1000
    if A <= 5:
        total += po * 5
    elif A <= 10:
        total += po * 6
    else:
        total += po * 7

elif H == "G":
    total += 500
    if A <= 5:
        total += po * 4
    elif A <= 10:
        total += po * 5
    else:
        total += po * 6

print(f"{total:.0f}")
