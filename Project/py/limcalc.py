import numpy as np
import matplotlib.pyplot as plt
import atlas_mpl_style as ampl
import matplotlib.cm as cm
import scipy
from scipy import interpolate
from sympy import *
from sympy import pi
import sympy as sym
import sys
import math

ma = sym.symbols('ma')
czh_l = sym.symbols('czh_l')
mh = 125     #GeV
mz = 91     #GeV
v = 246     #GeV
cah_l2 = czh_l

b = 2*czh_l**2*mh**6*((-4*ma**2*mz**2 + (-ma**2 + mh**2 - mz**2)**2)/mh**4)**1.5/(cah_l2**2*v**2*((-4*ma**2 + mh**2)/mh**2)**0.5*(2*ma**2 - mh**2)**2 + 2*czh_l**2*mh**6*((-4*ma**2*mz**2 + (-ma**2 + mh**2 - mz**2)**2)/mh**4)**1.5 + 130816.0*pi*mh**3)

f = sym.simplify(b)
print(f)

2.0*y**2*(-33124*x**2 + (7344 - x**2)**2)**1.5/(484.128*y**2*(15625 - 4*x**2)**0.5*(2*x**2 - 15625)**2 + 2.0*y**2*(-33124*x**2 + (7344 - x**2)**2)**1.5 + 255500000000.0*pi)