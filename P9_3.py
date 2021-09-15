Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from sympy import *
>>> C=Matrix([[1,-6,3],[3,-1,1],[-1,9,1]])
>>> C
Matrix([
[ 1, -6, 3],
[ 3, -1, 1],
[-1,  9, 1]])
>>> P,D=C.diagonalize()
>>> P
Matrix([
[ 3, -13/14 + sqrt(83)*I/14, (-5*sqrt(83) + 29*I)/(2*(sqrt(83) - 22*I))],
[ 4,  -8/21 - sqrt(83)*I/21,      (-sqrt(83) + 13*I)/(3*(sqrt(83) - I))],
[11,                      1,                                          1]])
>>> D
Matrix([
[4,                   0,                   0],
[0, -3/2 - sqrt(83)*I/2,                   0],
[0,                   0, -3/2 + sqrt(83)*I/2]])
>>> D=Matrix([[1,-1,1],[-1,1,1][1,-1,1]])
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    D=Matrix([[1,-1,1],[-1,1,1][1,-1,1]])
TypeError: list indices must be integers or slices, not tuple
>>> d=Matrix([[1,-1,1][-1,1,1][1,-1,1]])
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    d=Matrix([[1,-1,1][-1,1,1][1,-1,1]])
TypeError: list indices must be integers or slices, not tuple
>>> d