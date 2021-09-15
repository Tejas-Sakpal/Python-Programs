Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from pylab import*
>>> import numpy as np
>>> from math import*
>>> x = np.linspace(0, 4*(np.pi))
>>> y = np.exp(-0.4*x)*np.sin(x)
>>> plot(x, y,label="$e^-0.4*x\sin*$")
[<matplotlib.lines.Line2D object at 0x000002585650EC40>]
>>> legend()
<matplotlib.legend.Legend object at 0x000002585851CE50>
>>> show()

================================ RESTART: Shell ================================
>>> import matplotlib.pyplot as plt
>>> import numpy as np
>>> x = np.arange(-5, 5)
>>> y = np.sin(x)*(1/1+(x**2))
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x000001EFE026DB20>]
>>> plt.show()

================================ RESTART: Shell ================================
>>> from math import *
>>> import numpy as np
>>> x = np.linspace(-2*(np.pi), 2*(np.pi))
>>> y1 = np.sin(x)
>>> y2 = np.cos(x)
>>> subplot(2,1,1)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    subplot(2,1,1)
NameError: name 'subplot' is not defined
>>> import matplotlib.pyplot as plt
>>> subplot(2,1,1)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    subplot(2,1,1)
NameError: name 'subplot' is not defined
>>> from pylab import *
>>> subplot(2,1,1)
<AxesSubplot:>
>>> 
====================================================================== RESTART: Shell ======================================================================
>>> from pylab import *
>>> from math import *
>>> import numpy as np
>>> x = np.linspace(0, 4*(np.pi))
>>> y = np.exp(-0.4*x)*np.sin(x)
>>> plot(x, y,label="$e^-0.4*x\sin*$")
[<matplotlib.lines.Line2D object at 0x000002B330F6EC40>]
>>> legend()
<matplotlib.legend.Legend object at 0x000002B333AEDE20>
>>> show()

================================= RESTART: Shell =================================
>>> from pylab import *
>>> import numpy as np
>>> from math import* 
>>> x = np.linspace(0, 4*(np.pi))
>>> y = np.exp(-0.4*x)*np.sin(x)
>>> plot(x, y,label="$e^-0.4*x\sin*$")
[<matplotlib.lines.Line2D object at 0x000002117B2DFC40>]
>>> legend()
<matplotlib.legend.Legend object at 0x000002117DE2DB20>
>>> show()
>>> 
================================= RESTART: Shell =================================
>>> 