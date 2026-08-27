"""KAIMOOK"""
mok, n = input().split()
tea, s, t = input().split()

nam = float(n)
nut = float(t)
CAL = 0.0

if tea == "R":
    if s == "1":
        CAL += 12 * nut
    elif s == "2":
        CAL += 18 * nut
    elif s == "3":
        CAL += 25 * nut
elif tea == "T":
    if s == "1":
        CAL += 15 * nut
    elif s == "2":
        CAL += 20 * nut
    elif s == "3":
        CAL += 30 * nut
elif tea == "M":
    if s == "1":
        CAL += 10 * nut
    elif s == "2":
        CAL += 15 * nut
    elif s == "3":
        CAL += 20 * nut

if mok == "H":
    CAL += 5 * nam
elif mok == "O":
    CAL += 3 * nam
elif mok == "J":
    CAL += 2 * nam

if CAL.is_integer():
    print(int(CAL))
else:
    print(CAL)
