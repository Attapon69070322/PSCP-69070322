
"""JAYAKPAINAIWAMENG"""
n, sym = map(str, input().split())
n1 = int(n)
if sym == "#":
    for r in range(n1):
        for c in range(n1):
            if r == c or r + c == n1-1:
                print(sym,end="")
            else:
                print("-",end="")
        print()
else:
    for r in range(n1):
        c1 = chr(ord(sym) + abs(r - n1 // 2))
        for c in range(n1):
            if r == c or r + c == n1-1:
                print(c1,end="")
            else:
                print("-",end="")
        print()
