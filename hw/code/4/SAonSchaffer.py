from __future__ import print_function, unicode_literals
from __future__ import absolute_import, division
from random import uniform,randint
import numpy as np

dig=5

class digit(object):


    def __init__(self):
        self.x=[]
        self.num=0
        for i in range(0,dig+1):
            self.x.append(randint(0,9))
        self.getnum()

    def getnum(self):
        self.num=0
        for i in range(1,dig+1):
            self.num+=self.x[i]*10**(4-i)
        if self.x[0]%2==1:
            self.num=-self.num

    def copy(self,other):
        self.x=other.x
        self.num=other.num





def schaffer(x):
    f1=x**2
    f2=(x-2)**2
    return f1+f2

def energy(x):
    rang=(10**5+2)**2+10**10
    return x/rang

def probability(en,e,T):
    return np.e**(-((en-e))/T**4)

def neighbor(x):
    xn=digit()
    xn.copy(x)
    i=randint(0,dig)
    xn.x[i]+=(-1)**(randint(0,1))
    xn.x[i]=xn.x[i]%10
    xn.getnum()
    return xn


def simulated_annealing(kmax,linewidth):

    s=digit()
    sb=digit()
    sb.copy(s)                                # Initialization
    e=energy(schaffer(s.num))
    eb=e
    sn=digit()

    for k in range(1,kmax+1):
        T=(kmax+1-k)/kmax
        sn=neighbor(s)
        en=energy(schaffer(sn.num))
        if k%linewidth==1:
            print(", %4d, : %7.1f, " %(k,sb.num),end="")
        if en<eb:
            sb.copy(sn)
            eb=en
            s.copy(sn)
            e=en
            print("!",end="")
        elif en<e:
            s.copy(sn)
            e=en
            print("+",end="")
        elif probability(en,e,T)>uniform(0,1):
            s.copy(sn)
            e=en
            print("?",end="")
        else:
            print(".",end="")
        if k%linewidth==0:
            print("")

    return sb


if __name__ == '__main__':
    kmax=100000
    linewidth=25
    sb=simulated_annealing(kmax,linewidth)
    print("x: %s, " %sb.num,"f1: %s, " %sb.num**2,"f2: %s" %(sb.num-2)**2,"steps: %s" %kmax)

