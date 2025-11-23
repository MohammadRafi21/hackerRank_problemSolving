from collections import Counter
no_of_shoes = int(input())
sizes_of_shoes = list(map(int,input().split()))
sizes_of_shoes = sizes_of_shoes[:no_of_shoes]
coll_of_shoes = Counter(sizes_of_shoes)
total_money = 0
no_of_customer = int(input())

for i in range(no_of_customer):
    inquiry_size, money = map(int,input().split())
    if coll_of_shoes[inquiry_size] > 0:
        total_money += money
        coll_of_shoes[inquiry_size] -=1
    else:
        continue
print(total_money)