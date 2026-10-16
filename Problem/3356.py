"""BUSSING"""
seats_per_col = int(input())
num_cols = int(input())
target = int(input())

for pos in range(seats_per_col, 0, -1):
    row_seats = []
    for col in range(1, num_cols + 1):
        seat_num = (col - 1) * seats_per_col + pos
        if seat_num == target:
            row_seats.append("XX")
        else:
            row_seats.append(f"{seat_num:02d}")

    print(" ".join(row_seats))

    if pos % 2 == 1 and pos > 1:
        print()
