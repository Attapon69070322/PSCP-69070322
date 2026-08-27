"""ATM"""
m = int(input())
T = 0
H = 0
R = 0

if m <= 0 or m % 100:
    print("ERROR")
elif m >= 100:
    T = m // 1000
    T1 = abs((T * 1000) - m)
    H = T1 // 500
    H1 = abs((H * 500) - T1)
    R = H1 // 100
    if T:
        print(f"1000 = {T}")
    if H:
        print(f"500 = {H}")
    if R:
        print(f"100 = {R}")
