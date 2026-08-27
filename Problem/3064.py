"""Birthday"""
from datetime import date

y1 = int(input())
m1 = int(input())
d1 = int(input())
y2 = int(input())
m2 = int(input())
d2 = int(input())
de1 = date(y1, m1, d1)
de2 = date(y2, m2, d2)
diff = abs((de1 - de2).days)
if diff <= 7:
    print(0)
elif de1 < de2:
    print(1)
else:
    print(2)
