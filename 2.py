Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from mpl_toolkits import mplot3d
>>> import numpy as np

>>> from pylab import*
>>> def f(x, y):
	return np.sin(x+y)

>>> x = np.linspace(-2*(np.pi), 2*(np.pi))
>>> y = np.linspace(-2*(np.pi), 2*(np.pi))

>>> x, y = np.meshgrid(x, y)
>>> z = f(x,y)

>>> ax = axes(projection='3d')
>>> ax.contour3D(x, y, z, 50)
<matplotlib.contour.QuadContourSet object at 0x0000023C52A8A310>
>>> xlabel('x')

Text(0.5, 0, 'x')
>>> ylabel('y')
Text(0.5, 0, 'y')
>>> title('3D contour')
Text(0.5, 0.92, '3D contour')
>>> legend()

No handles with labels found to put in legend.
<matplotlib.legend.Legend object at 0x0000023C5007D340>
>>> show()
>>> 
=============================== RESTART: Shell ==============================
>>> from mpl_toolkits import mplot3d
>>> import numpy as n
>>> from pylab import*

>>> from math import*
>>> def f(x, y):
	return x**3+y**2

>>> x = n.linspace(0, 2*(n.pi))
>>> y = n.linspace(0, 2*(n.pi))
>>> X, Y = n.meshgrid(x, y)
>>> Z = f(X, Y)
>>> > ax = axes(projection='3d')
SyntaxError: invalid syntax
>>> ax = axes(projection='3d')
>>>  ax.contour3D(X, Y, Z, 50)
 
SyntaxError: unexpected indent
>>> ax.contour3D(X, Y, Z, 50)
<matplotlib.contour.QuadContourSet object at 0x00000242B303B2E0>
>>> xlabel("x")
Text(0.5, 0, 'x')
>>> ylabel("y")
Text(0.5, 0, 'y')
>>> title("3D contour")
Text(0.5, 0.92, '3D contour')
>>> legend()
No handles with labels found to put in legend.
<matplotlib.legend.Legend object at 0x00000242B05CC820>
>>> show()

=============================== RESTART: Shell ==============================
>>> from mpl_toolkits import mplot3d
>>> import numpy as np
>>> from pylab import *
>>> def f(x, y):
	return np.sin(x)+np.cos(y)

>>> x = np.linspace(-2*(np.pi), 2*(np.pi))

>>> y = np.linspace(-2*(np.pi), 2*(np.pi))
>>> X, Y = np.meshgrid(x, y)
>>> Z = f(X, Y)
>>> ax = axes(projection='3d')
>>> ax.contour3D(X, Y, Z, 50)

<matplotlib.contour.QuadContourSet object at 0x00000280E8AEB2E0>
>>> xlabel("x")
Text(0.5, 0, 'x')
>>> ylabel("y")
Text(0.5, 0, 'y')
>>> title("3D contour")
Text(0.5, 0.92, '3D contour')
>>> legend()
No handles with labels found to put in legend.
<matplotlib.legend.Legend object at 0x00000280E60E7310>
>>> show()

=============================== RESTART: Shell ==============================
>>> from mpl_toolkits import mplot3d
>>> import numpy Aas np
SyntaxError: invalid syntax
>>> import numpy as np
>>> from pylab import *
>>> from math import *
>>> def f(x,y):
	return np.exp(x**2+y**2)

>>> x = np.linspace(0, 2*(np.pi))
>>> y = np.linspace(0, 2*(np.pi))
>>> X, Y = np.meshgrid(x, y)
>>> Z = f(X, Y)
>>> ax = axes(projection='3d')

>>> ax.plot_wireframe(X, Y, Z, rstride=2, cstride=2)
<mpl_toolkits.mplot3d.art3d.Line3DCollection object at 0x0000022DAB6CB340>
>>> xlabel("x")

Text(0.5, 0, 'x')
>>> ylabel("y")

Text(0.5, 0, 'y')
>>> title("$f(x,y)=e^{x^2+y^2}$")
Text(0.5, 0.92, '$f(x,y)=e^{x^2+y^2}$')
>>> legend()

No handles with labels found to put in legend.
<matplotlib.legend.Legend object at 0x0000022DAB6CB670>
>>> show()

=============================== RESTART: Shell ==============================
>>> from mpl_toolkits import mplot3d
>>> import numpy as np
>>> from pylab import*
>>> def f(x, y):
	return x**3+y**3+x**2+y**2+x+y+5

>>> x = np.linspace(-2, 2)

>>> y = np.linspace(-2, 2)
>>> X, Y = np.meshgrid(x, y)
>>> Z = f(X, Y)
>>> ax = axes(projection='3d')

>>> ax.plot_surface(X, Y, Z)
<mpl_toolkits.mplot3d.art3d.Poly3DCollection object at 0x0000024748639340>
>>> xlabel("x")
Text(0.5, 0, 'x')
>>> ylabel("y")
Text(0.5, 0, 'y')
>>> title("$f(x,y)={x^3+y^3+x^2+y^2+x+y+5}$")

Text(0.5, 0.92, '$f(x,y)={x^3+y^3+x^2+y^2+x+y+5}$')
>>> legend()
No handles with labels found to put in legend.
<matplotlib.legend.Legend object at 0x0000024748639280>
>>> show()
