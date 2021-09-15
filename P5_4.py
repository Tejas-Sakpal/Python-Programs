Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from sympy import *
>>> A=Matrix([[1,2,1,3],[2,1,-4,-5],[7,8,-5,-1],[10,14,-2,8]])
>>> A
Matrix([
[ 1,  2,  1,  3],
[ 2,  1, -4, -5],
[ 7,  8, -5, -1],
[10, 14, -2,  8]])
>>> A.rref()
(Matrix([
[1, 0, -3, -13/3],
[0, 1,  2,  11/3],
[0, 0,  0,     0],
[0, 0,  0,     0]]), (0, 1))
>>> A.rank()
2
>>> A.nullspace()
[Matrix([
[ 3],
[-2],
[ 1],
[ 0]]), Matrix([
[ 13/3],
[-11/3],
[    0],
[    1]])]
>>> A.columnspace()
[Matrix([
[ 1],
[ 2],
[ 7],
[10]]), Matrix([
[ 2],
[ 1],
[ 8],
[14]])]
>>> A.t
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    A.t
AttributeError: 'MutableDenseMatrix' object has no attribute 't'
>>> A.T
Matrix([
[1,  2,  7, 10],
[2,  1,  8, 14],
[1, -4, -5, -2],
[3, -5, -1,  8]])
>>> A.inv()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    A.inv()
  File "C:\Users\Tejas\AppData\Local\Programs\Python\Python39\lib\site-packages\sympy\matrices\matrices.py", line 2159, in inv
    return _inv(self, method=method, iszerofunc=iszerofunc,
  File "C:\Users\Tejas\AppData\Local\Programs\Python\Python39\lib\site-packages\sympy\matrices\inverse.py", line 459, in _inv
    rv = M.inverse_GE(iszerofunc=iszerofunc)
  File "C:\Users\Tejas\AppData\Local\Programs\Python\Python39\lib\site-packages\sympy\matrices\matrices.py", line 2144, in inverse_GE
    return _inv_GE(self, iszerofunc=iszerofunc)
  File "C:\Users\Tejas\AppData\Local\Programs\Python\Python39\lib\site-packages\sympy\matrices\inverse.py", line 245, in _inv_GE
    raise NonInvertibleMatrixError("Matrix det == 0; not invertible.")
sympy.matrices.common.NonInvertibleMatrixError: Matrix det == 0; not invertible.
>>> 