"""Out ta ma mind"""
from decimal import Decimal, ROUND_HALF_UP
n = int(input())
total = 0
ft = n * 0.50
if n <= 10:
    total = n * 5
elif n <= 50:
    total = (10 * 5) + ((n - 10)*7)
elif n <= 100:
    total = (40 * 7) + (10 * 5) + ((n - 50)*10)
elif n <= 200:
    total = (50 * 10) + (40 * 7) + (10 * 5) + ((n - 100)*12)
else:
    total = (50 * 10) + (40 * 7) + (10 * 5) + (100 * 12) + ((n - 200)*15)

vat = total * 0.07
total = Decimal(str(total + vat + ft))
ans = total.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
print(ans)
