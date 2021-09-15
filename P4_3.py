Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def divisors(x):
	for i in range(1,x+1):
		if x%i==0:
			print(i,end=',')

			
>>> divisors(200)
1,2,4,5,8,10,20,25,40,50,100,200,
>>> 