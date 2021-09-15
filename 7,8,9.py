Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from sympy import *
>>> p1,p2,p3,p4=[(0,0),(1,0),(2,2),(1,4)]
>>> P=Polygon(p1,p2,p3,p4)
>>> P
Polygon(Point2D(0, 0), Point2D(1, 0), Point2D(2, 2), Point2D(1, 4))
>>> P.area
4
>>> P.perimeter
1 + sqrt(17) + 2*sqrt(5)
>>> 
=================================== RESTART: Shell ===================================
>>> P=Polygon((0,0),6,n=4)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    P=Polygon((0,0),6,n=4)
NameError: name 'Polygon' is not defined
>>> from sympy import *
>>> P=Polygon((0,0),6,n=4)
>>> P
RegularPolygon(Point2D(0, 0), 6, 4, 0)
>>> P.area
72
>>> P.perimeter
24*sqrt(2)
>>> 
=================================== RESTART: Shell ===================================
>>> P=RegularPolygon(Point(-1,2),2,8)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    P=RegularPolygon(Point(-1,2),2,8)
NameError: name 'RegularPolygon' is not defined
>>> from sympy import *
>>> P=RegularPolygon(Point(-1,2),2,8)
>>> P.center
Point2D(-1, 2)
>>> P.perimeter
16*sqrt(2 - sqrt(2))
>>> 
=================================== RESTART: Shell ===================================
>>> from sympy import *
>>> P=Polygon((-2,2),6,n=7)
>>> P
RegularPolygon(Point2D(-2, 2), 6, 7, 0)
>>> x,y=symbols('x,y')
>>> l=Line(x-2*y-5)
>>> P.reflect(l)
RegularPolygon(Point2D(12/5, -34/5), -6, 7, -2*pi/7 + atan(4/3))
>>> 
=================================== RESTART: Shell ===================================
>>> from sympy import *
>>> p1,p2,p3,p4=map(Point,[(0,0),(-2,0),(5,5),(1,-6)])
>>> P=Polygon(p1,p2,p3,p4)
>>> P
Polygon(Point2D(0, 0), Point2D(-2, 0), Point2D(5, 5), Point2D(1, -6))
>>> P.rotate(pi)
Polygon(Point2D(0, 0), Point2D(2, 0), Point2D(-5, -5), Point2D(-1, 6))
>>> P.angles[p1]
acos(-sqrt(37)/37)
>>> P.angles[p2]
-acos(7*sqrt(74)/74) + 2*pi
>>> P.angles[p3]
-acos(83*sqrt(10138)/10138) + 2*pi
>>> P.angles[p4]
-acos(62*sqrt(5069)/5069) + 2*pi
>>> 
=================================== RESTART: Shell ===================================
>>> from sympy import *
>>> A=Point(1,1)
>>> B=Point(2,-3)
>>> C=Point(-1,5)
>>> T=Triangle(A,B,C)
>>> T
Triangle(Point2D(1, 1), Point2D(2, -3), Point2D(-1, 5))
>>> x,y=symbols('x,y')
>>> L=Line(x+y+3)
>>> T.reflect(L)
Triangle(Point2D(-4, -4), Point2D(0, -5), Point2D(-8, -2))
>>> 
=================================== RESTART: Shell ===================================
>>> from sympy import *
A=Point(1,-2)
>>> 
=================================== RESTART: Shell ===================================
>>> from sympy import *
>>> A=Point(1,-2)
>>> B=Point(4,-6)
>>> 
KeyboardInterrupt
>>> C=Point(-1,4)
>>> T=Triangle(A,B,C)
>>> T
Triangle(Point2D(1, -2), Point2D(4, -6), Point2D(-1, 4))
>>> T.rotate(pi/2)
Triangle(Point2D(2, 1), Point2D(6, 4), Point2D(-4, -1))
>>> 
=================================== RESTART: Shell ===================================
>>> from sympy import *
>>> A=Point(-1,0)
>>> B=Point(2,-1)
>>> C=Point(1,3)
>>> T=Triangle(A,B,C)
>>> T
Triangle(Point2D(-1, 0), Point2D(2, -1), Point2D(1, 3))
>>> x,y=symbols('x,y')
>>> L=Line(x-y+3)
>>> T.reflect(L)
Triangle(Point2D(-3, 2), Point2D(-4, 5), Point2D(0, 4))
>>> 
=================================== RESTART: Shell ===================================
>>> from sympy import *
>>> A=Point(-1,2)
>>> B=Point(2,5)
>>> C=Point(-1,7)
>>> T=Triangle(A,B,C)
>>> T
Triangle(Point2D(-1, 2), Point2D(2, 5), Point2D(-1, 7))
>>> T.rotate(3*pi/2)
Triangle(Point2D(2, 1), Point2D(5, -2), Point2D(7, 1))
>>> 
=================================== RESTART: Shell ===================================
>>> from sympy import *
>>> A=Point(0,1)
>>> B=Point(-5,0)
>>> C=Point(-3,3)
>>> T=Triangle(A,B,C)
>>> T
Triangle(Point2D(0, 1), Point2D(-5, 0), Point2D(-3, 3))
>>> T.area
-13/2
>>> T.perimeter
sqrt(26) + 2*sqrt(13)
>>> 
=================================== RESTART: Shell ===================================
>>> from sympy import *
>>> P=Point(1,0)
>>> Q=Point(2,3)
>>> R=Point(0,-2)
>>> T=Triangle(P,Q,R)
>>> T
Triangle(Point2D(1, 0), Point2D(2, 3), Point2D(0, -2))
>>> T.angles[P]
acos(-7*sqrt(2)/10)
>>> T.angles[Q]
acos(17*sqrt(290)/290)
>>> T.angles[R]
acos(12*sqrt(145)/145)
>>> 