number = input().split()
numlist = list(map(float, number))

def sumavg(sumy):

    total = 0

    for i in sumy:
        total += i

    print (sumy)

sumavg(numlist)
