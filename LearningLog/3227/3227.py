"""POKDENG"""
n = input().upper()
num = n[:-1]
name = n[-1]

if name == "D":
    if num == "A":
        num = "ace"
    elif num == "J":
        num = "jack"
    elif num == "Q":
        num = "queen"
    elif num == "K":
        num = "king"
    print(f"{num} of diamonds")
elif name == "H":
    if num == "A":
        num = "ace"
    elif num == "J":
        num = "jack"
    elif num == "Q":
        num = "queen"
    elif num == "K":
        num = "king"
    print(f"{num} of hearts")
elif name == "S":
    if num == "A":
        num = "ace"
    elif num == "J":
        num = "jack"
    elif num == "Q":
        num = "queen"
    elif num == "K":
        num = "king"
    print(f"{num} of spades")
elif name == "C":
    if num == "A":
        num = "ace"
    elif num == "J":
        num = "jack"
    elif num == "Q":
        num = "queen"
    elif num == "K":
        num = "king"
    print(f"{num} of clubs")
