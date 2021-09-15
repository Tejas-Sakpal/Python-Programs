Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from math import *
>>> x=int(input("Input an integer"))
Input an integer34
>>> y=float(input("Input a float value"))
Input a float value56.86
>>> x
34
>>> y
56.86
>>> print(x+y)
90.86
>>> print(x/y)
0.5979599015124868
>>> print(x%y)
34.0
>>> print(x*y)
1933.24
>>> print(x**2)
1156
>>> print(x**2)+(y**2)
1156
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print(x**2)+(y**2)
TypeError: unsupported operand type(s) for +: 'NoneType' and 'float'
>>> print((x**2)+(y**2))
4389.0596000000005
>>> print(x//y)
0.0
>>> 