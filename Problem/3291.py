"""Right Arrow"""
def main():
    """main"""
    k = int(input())
    n = int(input())
    mid = n // 2

    for i in range(n):
        spaces = mid - abs(mid - i)
        print(" " * spaces + "*" * k)

main()
