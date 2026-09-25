""" BUU"""
def main():
    """main"""
    rabbit = input()
    u = 0
    maxu = 0
    for c in rabbit.lower():
        if c == "b":
            u = 0
        elif c == "u":
            u += 1
        if u > maxu:
            maxu = u
    if maxu >= 2:
        print("Yes",maxu)
    elif "b" in rabbit.lower():
        findb = rabbit.lower().rfind("b")
        new = rabbit[:findb + 1] + "U" * (len(rabbit) - (findb + 1))
        print(new)
    else:
        buu = ("BUU" * len(rabbit))[: len(rabbit)]
        print(buu)

main()
