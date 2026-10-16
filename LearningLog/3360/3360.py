"""BREAD > Key"""
w, h, m, n = map(int, input().split())

x_cuts = list(map(int, input().split()))
y_cuts = list(map(int, input().split()))

xs = [0] + sorted(x_cuts) + [w]
ys = [0] + sorted(y_cuts) + [h]

widths = [xs[i+1] - xs[i] for i in range(len(xs) - 1)]
heights = [ys[j+1] - ys[j] for j in range(len(ys) - 1)]

widths.sort(reverse=True)
heights.sort(reverse=True)

w1 = widths[0]
w2 = widths[1] if len(widths) > 1 else 0
h1 = heights[0]
h2 = heights[1] if len(heights) > 1 else 0

first_area = w1 * h1
second_area = max(w1 * h2, w2 * h1)

print(f"{first_area} {second_area}")
