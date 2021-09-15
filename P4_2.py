number=int(input("Enter range"))
print("prime Numbers: ",end='')
for n in range(1,number):
    flag=0
    for i in range(2,number):
        if(n%i==0):
            break
        else:
            flag=1
    if flag==1:
        print(n,end=',')
        
        
