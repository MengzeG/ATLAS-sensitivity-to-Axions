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
mh = sym.symbols('mh')
mz = sym.symbols('mz')
v = sym.symbols('v')
cah_l2 = sym.symbols('cah_l2')

def Br(czh_l,ma):
    #mh = 125     #GeV
    #ma = np.linspace(0.0001,10,6)     #GeV
    #mz = 91     #GeV
    #v = 246     #GeV

    #czh_l = np.linspace(0.0002,0.0004,6)

    #cah_l2 = czh_l

    x = (mz/mh)**2
    y = (ma/mh)**2
    l = ((1-x-y)**2)-4*x*y     #lambda

    w_sm = 4.088*10**(-3)     #GeV
    w_hza = ((czh_l/1000)**2)*((mh**3)/(16*pi))*(l)**(3/2)     #GeV
    w_haa = ((cah_l2/1000)**2)*((v**2)*mh/(32*pi))*((1-2*(ma/mh)**2)**2)*(1-4*(ma/mh)**2)**(1/2)     #GeV

    Brhza = w_hza/(w_sm+w_hza+w_haa)
    Bragg = 1

    b = Brhza*Bragg

    return b


f = sym.simplify(Br(czh_l,ma))

print(f)
