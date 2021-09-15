def regulafalsi(f,x0,x1,e):
    x0=float(x0)
    x1=float(x1)
    e=float(e)
    if f(x0)*f(x1)>0.0:
        print("Root if equation does not lie in the given interval")
        print("Try again for different values")
    else:
        step=1
        condition=True
        while condition:
            x2=x0-(x1-x0)*f(x0)/(f(x1)-f(x0))
            print('Iteration %d,x2=%0.6f and f(x2)=%0.6f'%(step,x2,f(x2)))
            if f(x0)*f(x2)<0:
                      x1=x2
            else:
                 x0=x2
                 step=step+1
                 condition=abs(f(x2))>e
            print('\n Required root is:%0.8f'%x2)
