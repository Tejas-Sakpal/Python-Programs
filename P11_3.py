def trapazoidal(f,a,b,n):
    h=0.5
    result=.5*(f(a)+f(b))
    for i in range(1,n):
        result+=f(a+i*0.5)
    
    result *=0.5
    return result
   
