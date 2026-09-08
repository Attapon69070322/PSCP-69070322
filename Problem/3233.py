"""luck"""
t, t1 = map(str, input().split())
f, f1 = map(str, input().split())

if t == f and t1 == f1:
    print(1000000)
elif t == f and t1 != f1:
    print(0)
elif t != f and t1 == f1:
    print(100000)
elif t == f and t1[-3:] == f1[-3:]:
    print(2000)
elif t == f and t1[-2:] == f1[-2:]:
    print(1000)
elif t != f and t1[-3:] == f1[-3:]:
    print(200)
elif t != f and t1[-2:] == f1[-2:]:
    print(100)
elif t != f and t1 != f1:
    print(0)
