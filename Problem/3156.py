"""conan"""
s = input().lower()
k = int(input())
for _ in s:
    cha = ord(_) - ord("a")
    char = (cha + k) % 26
    print(chr(char + 97),end="")
