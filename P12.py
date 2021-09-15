#simpson's 1/3rd rule
def simpson13(f,a,b,n):
    h=float(b-a)/n
    result=f(a)+f(b)
    for i in range(1,n):
        k=a+i*h
        if i%2==0:
            result=result+2*f(k)
        else:
            result=result+4*f(k)
            result*=h/3
            return result
          


        
