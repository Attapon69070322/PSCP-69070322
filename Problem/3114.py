"""SUWANNABUKHUMHEE"""

t = input().split(".")
h = int(t[0])
m = int(t[1])
t1 = input().split(".")
h1 = int(t1[0])
m2 = int(t1[1])
first = (h * 60) + m
last = (h1 * 60) + m2
bet = last - first
CHECKt = (0 <= h <= 23) and (0 <= m <= 59)
CHECKt1 = (0 <= h1 <= 23) and (0 <= m2 <= 59)

if not CHECKt or not CHECKt1 or bet < 0:
    print("ERROR")
elif bet <= 15:
    print("FREE")
else:
    hour = bet // 60
    if bet % 60 > 0:
        hour += 1

    if hour == 1:
        print(25)
    elif hour == 2:
        print(50)
    elif hour == 3:
        print(80)
    elif hour == 4:
        print(110)
    elif hour == 5:
        print(145)
    elif hour == 6:
        print(180)
    elif 7 <=hour <= 24:
        print(250)
