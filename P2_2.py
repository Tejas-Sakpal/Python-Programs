Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from math import *
>>> def sphere():
	r=float(input("Enter radius of sphere"))
	v=(4/3)*(pi*(r**3))
	a=4*pi*r**2
	print("volume=",v,"\n area",a)

	
>>> sphere()
Enter radius of sphere2
volume= 33.510321638291124 
 area 50.26548245743669
>>> 