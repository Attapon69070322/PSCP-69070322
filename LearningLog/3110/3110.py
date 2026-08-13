"""songduan"""
x1 ,x2 = input().split()
w = float(input())
if x1 == "BKK" and x2 == "CNX":
    T = 10
    w = w * 30
    total = w + T
    print(f"{total:.2f}")
elif x1 == "CNX" and x2 == "UBP":
    T = 15
    w = w * 40
    total = w + T
    print(f"{total:.2f}")
elif x1 == "UBP" and x2 == "BKK":
    T = 20
    w = w * 40
    total = w + T
    print(f"{total:.2f}")
elif x1 == "BKK" and x2 == "PKT":
    T = 25
    w = w * 50
    total = w + T
    print(f"{total:.2f}")
elif x1 == "PKT" and x2 == "CNX":
    T = 30
    w = w * 60
    total = w + T
    print(f"{total:.2f}")
elif x1 == "UBP" and x2 == "PKT":
    T = 40
    w = w * 70
    total = w + T
    print(f"{total:.2f}")
else:
    print("Error")
