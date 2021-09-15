def trapazoidal(f,a,b,n):
    h=float(b-a)/n
    result=.5*(f(a)+f(b))
    for i in range(1,n):
        result+=f(a+i*h)
        result *=h
        return result



    
