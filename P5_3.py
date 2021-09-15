Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from sympy import *
>>> A=Matrix([[-5,2,3,4],[1,-1,9,0],[10,13,-11,6]])
>>> A
Matrix([
[-5,  2,   3, 4],
[ 1, -1,   9, 0],
[10, 13, -11, 6]])
>>> A.col_del(3)
>>> A
Matrix([
[-5,  2,   3],
[ 1, -1,   9],
[10, 13, -11]])
>>> A.row_del(1)
>>> A
Matrix([
[-5,  2,   3],
[10, 13, -11]])
>>> A=A.row_insert(2,Matrix([[7,-8,2]]))
>>> A
Matrix([
[-5,  2,   3],
[10, 13, -11],
[ 7, -8,   2]])
>>> 