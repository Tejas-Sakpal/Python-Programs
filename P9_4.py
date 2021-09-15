Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from sympy import *
>>> A=Matrix([[1,-1,1],[-1,1,1],[1,-1,1]])
>>> A
Matrix([
[ 1, -1, 1],
[-1,  1, 1],
[ 1, -1, 1]])
>>> P,D=A.diagonalize()
>>> P
Matrix([
[1, 1, 1],
[1, 1, 0],
[0, 1, 1]])
>>> D
Matrix([
[0, 0, 0],
[0, 1, 0],
[0, 0, 2]])
>>> 