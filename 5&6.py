Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from sympy import *
>>> x,y=symbols('x,y')
>>> l=Line(x-y-3)
>>> points=l.points
>>> p=points[0]
>>> q=points[1]
>>> M=Matrix([[1,3,0],[2,2,0],[0,0,1]])
>>> N=M.inv()
>>> p1=p.transform(N)
>>> q1=q.transform(N)
>>> l1=Line(p1,q1)
>>> l1.equation()
x + 3/2
>>> 
============================== RESTART: Shell ==============================
>>> from sympy import *
>>> A=Point(4,1)
>>> B=Point(-3,0)
>>> S=Segment(A,B)
>>> S=S.rotate(pi)
>>> S=S.scale(3,0)
>>> points=S.points
>>> p=points[0]
>>> q=points[1]
>>> p1=p.transform(Matrix([[0,1,0],[1,0,0],[0,0,1]]))
>>> q1=q.transform(Matrix([[0,1,0],[1,0,0],[0,0,1]]))
>>> Segment(p1,q1)
Segment2D(Point2D(0, -12), Point2D(0, 9))
>>> 
============================== RESTART: Shell ==============================
>>> from sympy import*
>>> from matplotlib import
SyntaxError: invalid syntax
>>> from matplotlib import *
>>> A=Point(2,-3)
>>> B=Point(1,2)
>>> C=Point(3,-1)
>>> T=Triangle(A,B,C)
>>> T=T.scale(-1.2)
>>> P=Point(0,1)
>>> Q=Point(2,3)
>>> L=Line(P,Q)
>>> T=T.reflect(L)
>>> T.rotate(3*pi/2)
Triangle(Point2D(-7/5, 4), Point2D(-1/5, -1), Point2D(-13/5, 2))
>>> 