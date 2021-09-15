Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from sympy import *
>>> A=Matrix([[1,2,3],[2,1,3],[3,3,6]])
>>> A
Matrix([
[1, 2, 3],
[2, 1, 3],
[3, 3, 6]])
>>> P,D=A.diagonalize()
>>> P
Matrix([
[-1, -1, 1],
[ 1, -1, 1],
[ 0,  1, 2]])
>>> D
Matrix([
[-1, 0, 0],
[ 0, 0, 0],
[ 0, 0, 9]])
>>> B=Matrix([[-1,4,-2],[-3,4,0],[-3,1,3]])
>>> B
Matrix([
[-1, 4, -2],
[-3, 4,  0],
[-3, 1,  3]])
>>> P,D=B.diagonalize()
>>> P
Matrix([
[1, 2, 1],
[1, 3, 3],
[1, 3, 4]])
>>> D
Matrix([
[1, 0, 0],
[0, 2, 0],
[0, 0, 3]])
>>> C=Matrix([[1,-6,3],[3,-1,1],[-1,9,-1]])
>>> C
Matrix([
[ 1, -6,  3],
[ 3, -1,  1],
[-1,  9, -1]])
>>> P,D=C.diagonalize()































>>> 
>>> 
>>> P

>>> 