Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=========== RESTART: C:/Users/Tejas/Desktop/Programs/Python/P12_4.py ===========
>>> from math import *
>>> def f(x):
	return cos(x)/x

>>> simpson38(f,0.1,0.5,6)
0.3579433930808523
>>> 