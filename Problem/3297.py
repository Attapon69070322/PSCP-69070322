"""looll"""
num = int(input())
total = 0
while num > 0:
    age ,ticket = map(int ,input().split())
    if age >= 15:
        cost = 150
        if 15 <= age <= 22:
            cost = 150 * 0.8
        elif age >= 60:
            cost = 150 * 0.5
        elif 22 <= age <= 60:
            cost = 150
    else:
        print(-1)
        continue
    if num < ticket:
        print(-2)
        continue
    total = cost * ticket
    num -= ticket
    print(int(total), num)
