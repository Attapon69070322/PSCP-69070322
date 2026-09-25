"""สมดุลย์ชีวิต"""
work = int(input())
working = [int(input()) for _ in range(work)]
noi = []
mak = []
for i in working:
    if i <= 18:
        noi.append(i)
    else:
        mak.append(i)
print(work + max(0, len(mak) - len(noi) - 1))
