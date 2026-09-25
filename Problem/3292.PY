"""Arrow"""
def main():
    """main"""
    direc = input()
    n = int(input())
    p = 2 * n - 1
    mid = p // 2
    for char in direc:
        if char == "R":
            for i in range(p):
                spaces = 2 * (mid - abs(mid - i))
                print(" " * spaces + "*" * (1 + abs(mid - i)))
        elif char == "L":
            for i in range(p):
                spaces = 1 * (abs(mid - i))
                print(" " * spaces + "*" * (1 + abs(mid - i)))
        print("")

main()
