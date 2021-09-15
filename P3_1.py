Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def str():
	    s1=input('enter a string:')
	    s2=input('enter a string:')
	    print(3*s1+2*s2)
	    print(s1[1])
	    print(s1.upper())
	    print(s1[1:3])
	    print(s1[2]+s2[:2])
	    print(s1+s2[-1])
	    print('welcome',+s2)

	    
>>> str()
enter a string:Tejas
enter a string:Sakpal
TejasTejasTejasSakpalSakpal
e
TEJAS
ej
jSa
Tejasl
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    str()
  File "<pyshell#3>", line 10, in str
    print('welcome',+s2)
TypeError: bad operand type for unary +: 'str'
>>> 