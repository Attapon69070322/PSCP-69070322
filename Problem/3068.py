"""NEWYEAR"""
y = int(input())
anu = y % 100
tin = y % 400
president = y % 4

if not tin or (not president and anu) or (y < 1582 and not president):
    print("yes")
else:
    print("no")
