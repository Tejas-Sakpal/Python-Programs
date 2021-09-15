Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> def phi(n):
	i=0
	cnt=0
	for i in range(1,n):
		if math.gcd(n,i)==1:
			print(i,end=',')
			cnt=cnt+1
			i=i+i
	print('\n phi(',n,')',cnt)

	
>>> phi(20)
1,3,7,9,11,13,17,19,
 phi( 20 ) 8
>>> 