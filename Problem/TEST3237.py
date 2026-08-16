"""triangle"""
num = int(input())
i = 1 
for i in range(1 , num+1):
    for j in range(1 ,i+1):
        if i == j or j == 1 or i == num:
            print("0" , end ="")
        else:
            print("1" , end ="")
    print()

