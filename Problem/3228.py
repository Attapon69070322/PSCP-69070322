"""SARAAA"""
n = input().lower()
score = 0
k = ["a","e","i","o","u"]
for i in n:
    if i in k:
        score +=1

print(score)
