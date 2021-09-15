Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from math import *
>>> def distance(x1,x2,y1,y2):
	distance=sqrt((x2-x1)**2+(y2-y1)**2)
	print("Distance Between Two pOints= ",distance)

	
>>> distance(1,2,4,5)
Distance Between Two pOints=  1.4142135623730951
>>> 