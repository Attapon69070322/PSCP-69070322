"""SongOOk"""
n = int(input())
s = 0
ou =[]
ek =[]

for i in range(n):
    i += 1
    sin = int(input())
    s += sin
    sin = abs(sin)
    if not sin % 2:
        ek.append(sin)
    else:
        ou.append(sin)

print(f"SUM {s}")
print(f"EVEN {len(ek)}")
print(f"ODD {len(ou)}")
