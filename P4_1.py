Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a,b=0,1
>>> while a<1000:
	print(a,end=',')
	a,b=b,a+b

	
0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,
>>> 