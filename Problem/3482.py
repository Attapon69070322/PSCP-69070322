"""อาโป"""
QUEUE = [
    ["Spider Demon", 1],
    ["Swamp Demon", 2],
    ["Arrow Demon", 1],
    ["Hand Demon", 2],
    ["Drum Demon", 3],
    ["Mugen Train", 2],
    ["Upper Moon", 3],
]

KILLED = 0
TOTAL_ATTACKS = 0

while KILLED < 5:
    NAME, WEAKNESS = QUEUE.pop(0)
    print(NAME)
    KILLED_THIS_ROUND = False
    for _ in range(2):
        ATTACK = int(input())
        TOTAL_ATTACKS += 1
        if ATTACK == WEAKNESS:
            print("kill")
            KILLED += 1
            KILLED_THIS_ROUND = True
            break
    if not KILLED_THIS_ROUND:
        print("back")
        QUEUE.append([NAME, WEAKNESS])

print(TOTAL_ATTACKS)
