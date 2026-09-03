"""TESTSongkran"""
move = input()
med = len(move)
x = 0
y = 0
for i in range(med):
    if move[i] == "N":
        y += 1
    if move[i] == "S":
        y -= 1
    if move[i] == "E":
        x += 1
    if move[i] == "W":
        x -= 1

hattan = abs(x) + abs(y)
print(x , y , hattan)
