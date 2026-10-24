"""pair"""
n = input()
num = {}
for char in n:
    num[char] = num.get(char, 0) + 1

not_pair = []
for char, count in num.items():
    if count % 2:
        not_pair.append(char)

if not_pair:
    print("".join(not_pair))
else:
    print("fully paired")