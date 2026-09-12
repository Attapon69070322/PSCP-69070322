"""luck"""
t, t1 = input().split()
f, f1 = input().split()

if t == f and t1 == f1:
    print(1000000)
elif t != f and t1 == f1:
    print(100000)
elif t == f and t1[2:5] == f1[2:5]:
    print(2000)
elif t == f and t1[3:5] == f1[3:5]:
    print(1000)
elif t != f and t1[2:5] == f1[2:5]:
    print(200)
elif t != f and t1[3:5] == f1[3:5]:
    print(100)
elif t == f and t1 != f1:
    print(20)
elif t != f and t1 != f1:
    print(0)
