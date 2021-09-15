Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def Reverse(tuples):
	new_tuple=tuples[::-1]
	return new_tuple

>>> tuples=('a','b','c','d')
>>> print(Reverse(tuples))
('d', 'c', 'b', 'a')
>>> 