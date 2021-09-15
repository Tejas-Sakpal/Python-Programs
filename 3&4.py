Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> X=Point(6,7)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    X=Point(6,7)
NameError: name 'Point' is not defined
>>> from sympy import *
>>> X=Point(6,7)
>>> X.transform(Matrix([[1,7,0],[-3,1,0],[0,0,1]]))
Point2D(-15, 49)
>>> A=Point(6,6)
>>> B=Point(13,-100)
>>> C=Point(-19,-16)
>>> A.rotate(radians(45))
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    A.rotate(radians(45))
NameError: name 'radians' is not defined
>>> from math import *
>>> A.rotate(radians(45))
Point2D(7105427357601/8000000000000000000000000000, 848528137423857/100000000000000)
>>> A.rotate(radians(30))
Point2D(219615242270663/100000000000000, 819615242270663/100000000000000)
>>> A.rotate(radians(75))
Point2D(-424264068711929/100000000000000, 734846922834953/100000000000000)
>>> B.rotate(radians(45))
Point2D(799030662740799/10000000000000, -76897862454037/1250000000000)
>>> B.rotate(radians(30))
Point2D(612583302491977/10000000000000, -801025403784439/10000000000000)
>>> B.rotate(radians(75))
Point2D(249893075538099/2500000000000, -66624343842471/5000000000000)
>>> C.rotate(radians(45))
Point2D(-53033008588991/25000000000000, -61871843353823/2500000000000)
>>> C.rotate(radians(30))
Point2D(-422724133595217/50000000000000, -23356406460551/1000000000000)
>>> C.rotate(radians(75))
Point2D(26343128409193/2500000000000, -112468477105663/5000000000000)
>>> from sympy import*
>>> A=Point(-2,5)
>>> B=Point(4,3)
>>> A1=A.transform(Matrix([[2,2,0],[4,-1,0],[0,0,1]]))
>>> B1=B.transform(Matrix([[2,2,0],[4,-1,0],[0,0,1]]))
>>> L=Segment(A1,B1)
>>> L.midpoint
Point2D(18, -2)
>>> 
====================================================================== RESTART: Shell ======================================================================
>>> from sympy import*
>>> x,y=symbols('x,y')
>>> A=Point(-5,2)
>>> B=Point(3,-4)
>>> S=Segment(A,B)
>>> S.reflect(Line(2*x-y-1))
Segment2D(Point2D(27/5, -16/5), Point2D(-21/5, -2/5))
>>> 
====================================================================== RESTART: Shell ======================================================================
>>> 
====================================================================== RESTART: Shell ======================================================================
>>> from sympy import*
>>> A=Point(-1,8)
>>> B=Point(5,-6)
>>> A1=A.transform(Matrix([[3,-1,0],[5,3,0],[0,0,1]]))
>>> B1=B.transform(Matrix([[3,-1,0],[5,3,0],[0,0,1]]))
>>> S=Segment(A1,B1)
>>> S.slope
12/13
>>> 
====================================================================== RESTART: Shell ======================================================================
>>> x,y=symbols('x,y')
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    x,y=symbols('x,y')
NameError: name 'symbols' is not defined
>>> from sympy import *
>>> x,y=symbols('x,y')
>>> l1=Line(2*x+y)
>>> l2=Line(x-3*y-10)
>>> p=l1.intersection(l2)
>>> p=p[0]
>>> p.transform(Matrix([[2,-3,0],[1,-3,0],[0,0,1]]))
Point2D(0, 30/7)
>>> 
====================================================================== RESTART: Shell ======================================================================
>>> from sympy import *
>>> x,y=symbols('x,y')
>>> l=Line(2*x-y-8)
>>> points=l.points
>>> p=points[0]
>>> q=points[1]
>>> p1=p.transform(Matrix([[1,6,0],[4,1,0],[0,0,1]]))
>>> q1=q.transform(Matrix([[1,6,0],[4,1,0],[0,0,1]]))
>>> l1=Line(p1,q1)
>>> l1.equation()
-8*x + 9*y - 184
>>> 