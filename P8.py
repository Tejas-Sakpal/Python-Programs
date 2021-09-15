Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from sympy import *
>>> a=Matrix([[1,2,3],[0,1,0],[2,1,2]])
>>> a
Matrix([
[1, 2, 3],
[0, 1, 0],
[2, 1, 2]])
>>> a.eigenvals()
{4: 1, 1: 1, -1: 1}
>>> a.eigenvects()
[(-1, 1, [Matrix([
[-3/2],
[   0],
[   1]])]), (1, 1, [Matrix([
[ 1/4],
[-3/2],
[   1]])]), (4, 1, [Matrix([
[1],
[0],
[1]])])]
>>> b=Matrix([[2,1,1],[2,3,4],[-1,-1,2]])
>>> b
Matrix([
[ 2,  1, 1],
[ 2,  3, 4],
[-1, -1, 2]])
>>> b.eigenvals()
{1: 1, 3 - 2*I: 1, 3 + 2*I: 1}
>>> b.eigenvects()
[(1, 1, [Matrix([
[-1],
[ 1],
[ 0]])]), (3 - 2*I, 1, [Matrix([
[  -1/2 + I/2],
[-1/2 + 3*I/2],
[           1]])]), (3 + 2*I, 1, [Matrix([
[  -1/2 - I/2],
[-1/2 - 3*I/2],
[           1]])])]
>>> c=Matrix([[0,0,0],[0,0,0],[3,0,1]])
>>> c
Matrix([
[0, 0, 0],
[0, 0, 0],
[3, 0, 1]])
>>> c.eigenvals()
{0: 2, 1: 1}
>>> c.eigenvects()
[(0, 2, [Matrix([
[0],
[1],
[0]]), Matrix([
[-1/3],
[   0],
[   1]])]), (1, 1, [Matrix([
[0],
[0],
[1]])])]
>>> d=Matrix([[0,1,0],[0,0,1],[4,-17,8]])
>>> d
Matrix([
[0,   1, 0],
[0,   0, 1],
[4, -17, 8]])
>>> d.eigenvals()
{4: 1, 2 - sqrt(3): 1, sqrt(3) + 2: 1}
>>> d.eigenvects()
[(4, 1, [Matrix([
[1/16],
[ 1/4],
[   1]])]), (2 - sqrt(3), 1, [Matrix([
[1/(7 - 4*sqrt(3))],
[-1/(-2 + sqrt(3))],
[                1]])]), (sqrt(3) + 2, 1, [Matrix([
[1/(4*sqrt(3) + 7)],
[-1/(-2 - sqrt(3))],
[                1]])])]
>>> 