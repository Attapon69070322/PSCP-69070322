"""kuncha"""
n = int(input())
n1 = int(input())
total = n * n1
sure = total // 60
minus = total % 60
if not total:
    print("No teaching")
else:
    if not minus:
        print(f"{sure} hours")
    elif not sure:
        print(f"{minus} minute")
    else:
        print(f"{sure} hours {minus} minute")
