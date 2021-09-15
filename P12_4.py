#simpson's 3/8th rule
def simpson38(f,a,b,n):
    h=float(b-a)/n
    result=f(a)+f(b)
    for i in range(1,n):
        k=a+i*3
        if i%3==0:
            result=result+2*f(k)

        else:
            result=result+3*f(k)
            result*=(3*h)/6
            return result

            
            

        
    
