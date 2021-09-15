Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> def f(x):
	a=math.sin(x)
	b=math.cos(x)
	c=math.log(x)
	print('sin',x,'=',a)
	print('cos',x,'=',b)
	print('log',x,'=',c)

	
>>> f(2.6)
sin 2.6 = 0.5155013718214642
cos 2.6 = -0.8568887533689473
log 2.6 = 0.9555114450274363
>>> f(math.pi)
sin 3.141592653589793 = 1.2246467991473532e-16
cos 3.141592653589793 = -1.0
log 3.141592653589793 = 1.1447298858494002
>>> 