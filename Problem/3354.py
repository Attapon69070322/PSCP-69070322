"""nong nongkrub"""
import operator
ops = {
    "==":   operator.eq,
    "!=":   operator.ne,
    ">":    operator.gt,
    "<":    operator.lt,
    ">=":   operator.ge,
    "<=":   operator.le,
}
n1 ,num_n1 = input().split()
n2 ,num_n2 = input().split()
n3 ,num_n3 = input().split()

num_n1 = int(num_n1)
num_n2 = int(num_n2)
num_n3 = int(num_n3)

for h in range(10):
    if ops[n3](h, num_n3):
        for t in range(10):
            if ops[n2](t, num_n2):
                for u in range(10):
                    if ops[n1](u, num_n1):
                        print(f"{h}{t}{u}")
