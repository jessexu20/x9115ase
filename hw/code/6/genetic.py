from __future__ import print_function, unicode_literals
from __future__ import absolute_import, division
from random import uniform,randint,random,seed
from time import time
import numpy as np
from pdb import set_trace

class Model(object):
    def any(self):
        while True:
            for i in range(0,self.decnum):
                self.dec[i]=uniform(self.bottom[i],self.top[i])
            if self.check(): break

    def __init__(self):
        self.bottom=[0]
        self.top=[0]
        self.decnum=0
        self.objnum=0
        self.dec=[0]

    def eval(self):
        return sum(self.getobj())

    def copy(self,other):
        self.dec=other.dec[:]
        self.bottom=other.bottom[:]
        self.top=other.top[:]
        self.decnum=other.decnum
        self.objnum=other.objnum

    def getobj(self):
        return []

    def check(self):
        for i in range(0,self.decnum):
            if self.dec[i]<self.bottom[i] or self.dec[i]>self.top[i]:
                return False
        return True


class Osyczka2(Model):

    def __init__(self):
        self.bottom=[0,0,1,0,1,0]
        self.top=[10,10,5,6,5,10]
        self.decnum=6
        self.objnum=2
        self.dec=[0,0,0,0,0,0]
        self.any()

    def getobj(self):
        f1=-(25*(self.dec[0]-2)**2+(self.dec[1]-2)**2+((self.dec[2]-1)**2)*(self.dec[3]-4)**2+(self.dec[4]-1)**2)
        f2=self.dec[0]**2+self.dec[1]**2+self.dec[2]**2+self.dec[3]**2+self.dec[4]**2+self.dec[5]**2
        return [f1,f2]

    def check(self):
        g=[0,0,0,0,0,0]
        g[0]=self.dec[0]+self.dec[1]-2
        g[1]=6-self.dec[0]-self.dec[1]
        g[2]=2-self.dec[1]+self.dec[0]
        g[3]=2-self.dec[0]+3*self.dec[1]
        g[4]=4-self.dec[3]-(self.dec[2]-3)**2
        g[5]=(self.dec[4]-3)**3+self.dec[5]-4
        for i in range(0,self.decnum):
            if self.dec[i]<self.bottom[i] or self.dec[i]>self.top[i] or g[i]<0:
                return False
        return True

class Schaffer(Model):

    def __init__(self):
        self.bottom=[-10**5]
        self.top=[10**5]
        self.decnum=1
        self.objnum=2
        self.dec=[0]
        self.any()

    def getobj(self):
        f1=self.dec[0]**2
        f2=(self.dec[0]-2)**2
        return [f1,f2]



class Kursawe(Model):

    def __init__(self):
        self.bottom=[-5,-5,-5]
        self.top=[5,5,5]
        self.decnum=3
        self.objnum=2
        self.dec=[0,0,0]
        self.any()

    def getobj(self):
        f1=0
        f2=0
        for i in range(0,self.decnum):
            if i<self.decnum-1:
                f1+=-10*np.e**(-0.2*np.sqrt(self.dec[i]**2+self.dec[i+1]**2))
            f2+=np.abs(self.dec[i])**0.8+5*np.sin(self.dec[i])
        return [f1,f2]

def neighbor(s,index,model):
    sn=model()
    sn.copy(s)
    while True:
        sn.dec[index]=uniform(sn.bottom[index],sn.top[index])
        if sn.check(): break
    return sn

def simulated_annealing(model):

    def probability(en,e,T):
        return np.exp(-(((en-e)/max(np.abs(en),np.abs(e)))/T**3))

    s=model()
    sb=model()
    sb.copy(s)
    kmax=1000
    linewidth=50
    for k in range(0,kmax):
        T=(kmax+1-k)/kmax
        sn=neighbor(s,randint(0,s.decnum-1),model)
        if k%linewidth==1:
            print(", %4d, : %s, " %(k,sb.dec),end="")
        if sn.eval()<sb.eval():
            sb.copy(sn)
            s.copy(sn)
            print("!",end="")
        elif sn.eval()<s.eval():
            s.copy(sn)
            print("+",end="")
        elif probability(sn.eval(),s.eval(),T)>random():
            s.copy(sn)
            print("?",end="")
        else:
            print(".",end="")
        if k%linewidth==linewidth-1:
            print("")
    print("")
    print("Best solution: %s, " %sb.dec,"f1 and f2: %s, " %sb.getobj(),"steps: %s" %kmax)
    return True

def maxwalksat(model):

    def optc(s,which,step):
        sn=model()
        sn.copy(s)
        snbest=model()
        snbest.copy(sn)
        dis=(sn.top[which]-sn.bottom[which])/step
        for i in range(-int((s.dec[which]-s.bottom[which])/dis),int((s.top[which]-s.dec[which])/dis)+1):
            sn.dec[which]=sn.dec[which]+i*dis
            if not sn.check(): continue
            if sn.eval()<snbest.eval():
                snbest.copy(sn)
        return snbest

    eval=0
    evalx=0
    maxtries=10
    maxchanges=100
    threshold=-10000
    p=0.5
    step=10
    for i in range(0,maxtries):
        s=model()
        if i==0:
            sbest=model()
            sbest.copy(s)
        print(", Retries: %2d, : Best solution: %s, " %(i,sbest.dec),end="")
        for j in range(0,maxchanges):
            eval+=1
            if s.eval()<threshold:
                print("")
                print("Best solution: %s, " %s.dec,"f1 and f2: %s, " %s.getobj(),
                      "step * eval: %s * %s" %(step,eval),", at which eval the best x is found: %s" %eval)
                return True
            which=randint(0,s.decnum-1)
            score_old=s.eval()
            if p<random():
                s=neighbor(s,which,model)
            else:
                s=optc(s,which,step)
            if s.eval()<sbest.eval():
                sbest.copy(s)
                evalx=eval
                print("!",end="")
            elif s.eval()<score_old:
                print("+",end="")
            elif s.eval()==score_old:
                print(".",end="")
            else:
                print("?",end="")
        print("")
    print("Best solution: %s, " %sbest.dec,"f1 and f2: %s, " %sbest.getobj(),
          "step * eval: %s * %s" %(step,eval),", at which eval the best x is found: %s" %evalx)


if __name__ == '__main__':
    seed(time())
    for model in [Schaffer, Osyczka2, Kursawe]:
        for optimizer in [simulated_annealing, maxwalksat]:
            print("Optimizer: %s, " %optimizer.__name__,"Model: %s" %model.__name__)
            optimizer(model)