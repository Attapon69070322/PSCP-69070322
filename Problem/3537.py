"""DDDDDDDDDDDDTTDDDDDDDDTATDTADT"""
a = {}
d = {}

while True:
    line = input().strip()
    if line == "Start":
        break

    cleaned = line.strip("{}").replace('"', "").replace("'", "")
    name, role = cleaned.split(":")
    a[name.strip()] = role.strip()

while True:
    name = input().strip()
    if name == "End":
        break

    if name in a:
        d[name] = a.pop(name)

impostor = 0
for role in a.values():
    if role == "Impostor":
        impostor += 1

print(f"{impostor} Impostor Remains")

print("***Alive***")
for name in sorted(a.keys()):
    print(f"{name} : {a[name]}")

print("***Dead***")
for name in sorted(d.keys()):
    print(f"{name} : {d[name]}")
