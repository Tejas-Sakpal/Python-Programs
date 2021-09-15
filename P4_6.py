Numbers=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
count_even=0
count_odd=0
for x in Numbers:
    if not x%2:
        count_even=count_even+1
    else:
        count_odd=count_odd+1
print("Even Numbers are:",count_even)
print("Odd Numbers are:",count_odd)
