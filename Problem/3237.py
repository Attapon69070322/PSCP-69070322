"""Triangle"""
num = int(input())
P = "1"
for i in range (1 ,num+1):
    if num <= 3:
        print("0"*i)

    else:
        if i < 3:
            print("0"*i)
        elif i == num:
            print("0"*i)
        elif i >= 3:
            print(f"0{P*(i-2)}0")
