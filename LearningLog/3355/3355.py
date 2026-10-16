"""short"""
h = []
while True:
    n = int(input())
    if n == -1:
        break
    h.append(n)

if not h:
    print("")
else:
    result = []
    start = h[0]
    prev = h[0]

    for num in h[1:]:
        if num == prev + 1:
            prev = num
        else:
            if start == prev:
                result.append(str(start))
            else:
                result.append(f"{start}-{prev}")
            start = num
            prev = num

    if start == prev:
        result.append(str(start))
    else:
        result.append(f"{start}-{prev}")

    print(", ".join(result))
