"""กระต่าย flu"""

ROWS, COLS = map(int, input().split())
RABBIT_R, RABBIT_C = map(int, input().split())
N = int(input())

GRID = [[0] * COLS for _ in range(ROWS)]

for _ in range(N):
    INF_R, INF_C = map(int, input().split())
    for i in range(max(0, INF_R - 2), min(ROWS, INF_R + 3)):
        for j in range(max(0, INF_C - 2), min(COLS, INF_C + 3)):
            DIST = max(abs(i - INF_R), abs(j - INF_C))
            if not DIST:
                RISK = 100
            elif DIST == 1:
                RISK = 60
            else:
                RISK = 20
            if RISK > GRID[i][j]:
                GRID[i][j] = RISK

SAFE_COUNT = 0
for r in range(ROWS):
    for c in range(COLS):
        if not GRID[r][c]:
            SAFE_COUNT += 1

print(SAFE_COUNT)
print(f"{GRID[RABBIT_R][RABBIT_C]}%")
