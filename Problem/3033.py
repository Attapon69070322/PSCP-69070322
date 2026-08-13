"""bd"""
X1 ,Y1 ,Z1 = map(float, input().split())
wide = (2 * 3.14 * X1) + Z1
lenght = (X1 * 2) + Y1
print(f"{lenght:.2f} {wide:.2f}")
