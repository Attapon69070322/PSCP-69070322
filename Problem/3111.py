"""SAHAKORN"""
from decimal import Decimal, ROUND_HALF_UP
money = input()
n = int(input())
total = Decimal("0")
for i in range(n):
    i += 1
    cost = Decimal(input())
    total += cost
if money == "Y":
    total = total*Decimal("95")/Decimal("100")
elif money == "N":
    if total >= Decimal("500"):
        total = total*Decimal("97")/Decimal("100")
total = total.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
print(f"{total:.2f}")
