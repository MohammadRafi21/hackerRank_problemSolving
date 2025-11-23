from collections import Counter
no_of_shoes = int(input("Please enter how many shoes are there "))
sizes_of_shoes = list(map(int,input("Enter the size with a space ").split()))
sizes_of_shoes = sizes_of_shoes[:no_of_shoes]
coll_of_shoes = Counter(sizes_of_shoes)
total_money = 0
no_of_customer = int(input("Please enter the number of customer"))

for i in range(no_of_customer):
    inquiry_size = int(input("Please Enter what size you are looking for? "))
    if coll_of_shoes[inquiry_size] > 0:
        money = int(input("enter the money"))
        total_money += money
        coll_of_shoes[inquiry_size] -=1
    else:
        continue
print(total_money)
