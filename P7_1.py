Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from sympy import *
>>> a=Matrix([[1,1,1,1],[3,2,1,0],[27,9,3,1],[27,6,1,0]])
>>> a
Matrix([
[ 1, 1, 1, 1],
[ 3, 2, 1, 0],
[27, 9, 3, 1],
[27, 6, 1, 0]])
>>> b=Matrix([[3],[-5],[-7],[-1]])
>>> b
Matrix([
[ 3],
[-5],
[-7],
[-1]])
>>> a.gauss_jordan_solve(b)
(Matrix([
[ 1],
[-5],
[ 2],
[ 5]]), Matrix(0, 1, []))
>>> x,y,z,w=symbols("x,y,z,w")
>>> linsolve(a,b),[x,y,z,w])
SyntaxError: unmatched ')'
>>> linsolve((a,b),[x,y,z,w])
FiniteSet((1, -5, 2, 5))
>>> A=Matrix([[1,2,-3,-2,4],[2,5,-8,-1,6],[1,4,-7,5,2]])
>>> A
Matrix([
[1, 2, -3, -2, 4],
[2, 5, -8, -1, 6],
[1, 4, -7,  5, 2]])
>>> B=Matrix([[1],[4],[8]])
>>> B
Matrix([
[1],
[4],
[8]])
>>> A.gauss_jordan_solve(B)
(Matrix([
[-tau0 - 24*tau1 + 21],
[ 2*tau0 + 8*tau1 - 7],
[                tau0],
[          3 - 2*tau1],
[                tau1]]), Matrix([
[tau0],
[tau1]]))
>>> x1,x2,x3,x4,x5=symbols("x1,x2,x3,x4,x5")
>>> linsolve((A,B),[x1,x2,x3,x4,x5])
FiniteSet((-x3 - 24*x5 + 21, 2*x3 + 8*x5 - 7, x3, 3 - 2*x5, x5))
>>> C=Matrix([[0,1,3,-2],[2,1,-4,3],[2,3,2,-1],[-4,-3,5,-4]])
>>> C
Matrix([
[ 0,  1,  3, -2],
[ 2,  1, -4,  3],
[ 2,  3,  2, -1],
[-4, -3,  5, -4]])
>>> D=Matrix([[0],[0],[0],[0]])
>>> D
Matrix([
[0],
[0],
[0],
[0]])
>>> C.gauss_jordan_solve.(D)
SyntaxError: invalid syntax
>>> C.gauss_jordan_solve(D)
(Matrix([
[7*tau0/2 - 5*tau1/2],
[   -3*tau0 + 2*tau1],
[               tau0],
[               tau1]]), Matrix([
[tau0],
[tau1]]))
>>> u,v,w,x=symbols("u,v,w,x")
>>> linsolve((C,D),[u,v,w,x])
FiniteSet((7*w/2 - 5*x/2, -3*w + 2*x, w, x))
>>> 