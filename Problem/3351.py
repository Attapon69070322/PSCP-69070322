"""RABBIT LANGUINI"""

s_raw = input().strip()
s = s_raw.upper()
n = len(s)

if n > 0 and all(c in "TI" for c in s):
    print(f"unknown {n}")
    exit()

error_idx = -1
max_a = 0
curr_a = 0

for i in range(n):
    c = s[i]

    if c not in "RABIT":
        error_idx = i
        break

    if c == "A":
        curr_a += 1
        if curr_a > max_a:
            max_a = curr_a
    else:
        curr_a = 0

    if c == "A":
        if i == 0 or s[i - 1] not in "RA":
            error_idx = i
            break

    if c == "R":
        if i + 1 >= n or s[i + 1] != "A":
            error_idx = i + 1 if i + 1 < n else i
            break

    if c == "B":
        if i + 1 >= n or s[i + 1] not in "IT":
            error_idx = i + 1 if i + 1 < n else i
            break

if error_idx != -1:
    print(f"no {error_idx}")
else:
    print(f"yes {max_a}")
