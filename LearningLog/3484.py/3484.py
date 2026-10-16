"""Wall-e"""
line1 = input().split()
while not line1:
    line1 = input().split()

n = int(line1[0])
p = float(line1[1])

grid = []
while len(grid) < n:
    line = input().strip()
    if not line:
        continue
    grid.append([int(x) for x in line.split()])

for row in grid:
    bad_in_row = sum(1 for val in row if val > 0)
    print(*(row + [bad_in_row, sum(row)]))

bad_col = [sum(1 for r in range(n) if grid[r][c] > 0) for c in range(n)]
print(*bad_col)

sum_col = [sum(grid[r][c] for r in range(n)) for c in range(n)]
print(*sum_col)

total_bad = sum(bad_col)
total_pts = sum(sum_col)
fine = total_pts * p

print(f"{total_bad} {total_pts} {fine:.2f}")
