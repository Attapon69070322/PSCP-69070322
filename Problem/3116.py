"""NAVATAGAM"""
sch = input()
start = ord(sch[0].upper())
end = ord(sch[-1].upper())
n = len(sch)

Hlist = []

for i in range(10):
    if not i or not i % 2:
        Hlist.append(((i + start) % n) % 10)
    else:
        Hlist.append(((end - i) % n) % 10)

print(*Hlist[2:8])
