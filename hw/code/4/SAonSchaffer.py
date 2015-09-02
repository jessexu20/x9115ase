from __future__ import print_function, unicode_literals
from __future__ import absolute_import, division
from random import uniform
import numpy as np


def schaffer(x):
    f1=x**2
    f2=(x-2)**2
    return f1+f2

def energy(x):
    rang=(10**5+2)**2+10**10
    return x/rang

def probability(en,e,T):
    return np.e**(-((en-e)/abs(en))/T)

def neighbor(x):
    xmax=10**5
    xmin=-10**5
    xn=x*(10**uniform(-1,1))
    if uniform(0,1)>0.5:
        xn=-xn
    if xn>xmax:
        xn=xmax
    elif xn<xmin:
        xn=xmin
    return xn


def simulated_annealing(kmax,linewidth):

    s=uniform(-10**5,10**5)
    sb=s                                # Initialization
    e=energy(schaffer(s))
    eb=e


    for k in range(1,kmax+1):
        T=(kmax+1-k)/kmax
        sn=neighbor(s)
        en=energy(schaffer(sn))
        if k%linewidth==1:
            print(", %4d, : %1.10f, " %(k,eb),end="")
        if en<eb:
            sb=sn
            eb=en
            s=sn
            e=en
            print("!",end="")
        elif en<e:
            s=sn
            e=en
            print("+",end="")
        elif probability(en,e,T)>uniform(0,1):
            s=sn
            e=en
            print("?",end="")
        else:
            print(".",end="")
        if k%linewidth==0:
            print("")

    return sb


if __name__ == '__main__':
    kmax=1000
    linewidth=25
    sb=simulated_annealing(kmax,linewidth)
    print("x: %s, " %sb,"f1: %s, " %sb**2,"f2: %s" %(sb-2)**2)

