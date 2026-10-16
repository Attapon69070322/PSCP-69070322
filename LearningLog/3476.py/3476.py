"""Cute Cats and Foxes"""

import ast

n = int(input())

cats = {}
foxes = {}

for _ in range(n):
    line = input().strip()
    if not line:
        continue
    data = ast.literal_eval(line)

    for name, code in data.items():
        if code.startswith("Cat"):
            cats.update({code: name})
        elif code.startswith("Fox"):
            foxes.update({code: name})

all_names = list(cats.values()) + list(foxes.values())

if "Cat01" not in cats and "Garfield" not in all_names:
    cats.setdefault("Cat01", "Garfield")

if "Fox01" not in foxes and "Fubuki" not in all_names:
    foxes.setdefault("Fox01", "Fubuki")

print(f"Cat : {len(cats)}")
print(f"Fox : {len(foxes)}")

cat_keys = sorted(cats.keys(), key=lambda c: int(c[3:]))
for code in cat_keys:
    print(f"{cats.get(code)} : {code}")

fox_keys = sorted(foxes.keys(), key=lambda c: int(c[3:]))
for code in fox_keys:
    print(f"{foxes.get(code)} : {code}")
