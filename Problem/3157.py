"""GAME"""

n = int(input())
score = 0

for i in range(n):
    i += 1
    sym = input()
    if sym == "+":
        score += 10
    elif sym == "-":
        score -= 5

print(score)
