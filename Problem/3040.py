"""currency"""
money = float(input())
num10 = money // 10
money = money % 10
num5 = money // 5
money = money % 5
num2 = money // 2
money = money % 2
num1 = money

print(f"10 = {num10:.0f}")
print(f"5 = {num5:.0f}")
print(f"2 = {num2:.0f}")
print(f"1 = {num1:.0f}")
