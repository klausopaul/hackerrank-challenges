# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

stop = False

X = int(input())
if X > 0 and X < 10000:
    shoeSizes = input().split(" ")
    if len(shoeSizes) != X:
        print('Wrong number of shoe sizes. Stopping...', end="\n\n")
        stop = True
    else:
        shoeSizeInventory = Counter(shoeSizes)

if not(stop):
    N = int(input())
    if N <= 0 or N > 10000:
        print ("Wrong number of customers. Stopping...", end="\n\n")
        stop = True

if not(stop):
    sales = 0
    for i in range (N):
        neededShoe, pricePaid = input().split(" ")
        if shoeSizeInventory[neededShoe] > 0:
            sales += int(pricePaid)
            shoeSizeInventory[neededShoe] -= 1
    
    print (sales)
