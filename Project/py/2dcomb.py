# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import atlas_mpl_style as ampl
import matplotlib.cm as cm
import scipy
from scipy import interpolate
import sys
import math

filename1 = "\Beamdump.csv"
filename2 = "\CAST-SUMICO.csv"
filename3 = "\CDF.csv"
filename4 = "\cosmology.csv"
filename5 = "\g-2mu.csv"
filename6 = "\HB stars.csv"
filename7 = "\hza.csv"
filename8 = "\invgamma.csv"
filename9 = "\LEP.csv"
filename10 = "\LHC.csv"
filename11 = "\LHC2.csv"
filename12 = "\SN1987a.csv"

x1,y1 = np.loadtxt("./"+"\csv"+filename1, delimiter = ',', unpack=True)
x2,y2 = np.loadtxt("./"+"\csv"+filename2, delimiter = ',', unpack=True)
x3,y3 = np.loadtxt("./"+"\csv"+filename3, delimiter = ',', unpack=True)
x4,y4 = np.loadtxt("./"+"\csv"+filename4, delimiter = ',', unpack=True)
x5,y5 = np.loadtxt("./"+"\csv"+filename5, delimiter = ',', unpack=True)
x6,y6 = np.loadtxt("./"+"\csv"+filename6, delimiter = ',', unpack=True)
x7,y7 = np.loadtxt("./"+"\csv"+filename7, delimiter = ',', unpack=True)
x8,y8 = np.loadtxt("./"+"\csv"+filename8, delimiter = ',', unpack=True)
x9,y9 = np.loadtxt("./"+"\csv"+filename9, delimiter = ',', unpack=True)
x10,y10 = np.loadtxt("./"+"\csv"+filename10, delimiter = ',', unpack=True)
x11,y11 = np.loadtxt("./"+"\csv"+filename11, delimiter = ',', unpack=True)
x12,y12 = np.loadtxt("./"+"\csv"+filename12, delimiter = ',', unpack=True)






ma = np.linspace(0.7,9,100)     #GeV

def B(ma,czh_l):
    mh = 125     #GeV
    
    mz = 91     #GeV
    v = 246     #GeV
    cah_l2 = 0

    x = (mz/mh)**2
    y = (ma/mh)**2
    l = ((1-x-y)**2)-4*x*y     #lambda

    w_sm = 4.088*10**(-3)     #GeV
    w_hza = ((czh_l/1000)**2)*((mh**3)/(16*math.pi))*(l)**(3/2)     #GeV
    w_haa = ((cah_l2/1000)**2)*((v**2)*mh/(32*math.pi))*((1-2*(ma/mh)**2)**2)*np.sqrt(1-4*(ma/mh)**2)     #GeV

    Brhza = w_hza/(w_sm+w_hza+w_haa)
    Bragg = 1

    b = Brhza*Bragg
    
    plt.plot(ma, b,'--', label = 'C/\u039B ={}$TeV^{}$'.format(czh_l,-1))



B(ma,0.25)
B(ma,0.3)
B(ma,0.35)
B(ma,0.4)



plt.plot(ma1,exp, 'o',xf,yf,'--',label = 'expected upper limit')


plt.fill_between(ma1, y3,y4,color = '#00ff00',alpha= 1, label = '2\u03C3')
plt.fill_between(ma1, y1,y2,color = '#ffff00',alpha= 1, label = '1\u03C3')

plt.xlabel('$m_a$[GeV]')
plt.ylabel('BR(h \u2192 Za) \u00D7 BR(a \u2192 \u03B3\u03B3)')
plt.title('$C_{ah}=0$')
plt.legend()
plt.show()
