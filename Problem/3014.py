"""milk"""
bottle = int(input())
head = int(input())
head1 = int(input())
money = int(input())
buy = money // bottle
fah = buy
if head > 0:
    while fah >= head :
        gain = (fah // head) * head1
        gain1 = fah % head
        buy += gain
        fah += gain1 + gain

print(buy)
