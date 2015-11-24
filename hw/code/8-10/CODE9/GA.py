from __future__ import print_function, unicode_literals
from __future__ import absolute_import, division
from random import uniform,randint,random,seed
from time import time
import numpy as np
from pdb import set_trace
import pickle

from HVE import hve


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
        self.dec=[]
        self.lastdec=[]
        self.obj=[]
        self.any()

    def eval(self):
        return sum(self.getobj())

    def copy(self,other):
        self.dec=other.dec[:]
        self.lastdec=other.lastdec[:]
        self.obj=other.obj[:]
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


"Models:"
class DTLZ1(Model):
    def __init__(self,n=10,m=2):
        self.bottom=[0]*n
        self.top=[1]*n
        self.decnum=n
        self.objnum=m
        self.dec=[0]*n
        self.lastdec=[]
        self.obj=[]
        self.any()

    def getobj(self):
        if self.dec==self.lastdec:
            return self.obj
        f=[]
        g=self.decnum-self.objnum+1
        for x in self.dec[self.objnum-1:]:
            g=g+np.square(x-0.5)-np.cos((x-0.5)*20*np.pi)
        g=g*100
        for i in xrange(self.objnum):
            tmp=0.5*(1+g)
            for x in self.dec[:self.objnum-1-i]:
                tmp=tmp*x
            if not i==0:
                tmp=tmp*(1-self.dec[self.objnum-i])
            f.append(tmp)
        self.lastdec=self.dec
        self.obj=f
        return f

class DTLZ3(Model):
    def __init__(self,n=10,m=2):
        self.bottom=[0]*n
        self.top=[1]*n
        self.decnum=n
        self.objnum=m
        self.dec=[0]*n
        self.lastdec=[]
        self.obj=[]
        self.any()

    def getobj(self):

        if self.dec==self.lastdec:
            return self.obj

        f=[]
        g=self.decnum-self.objnum+1
        for x in self.dec[self.objnum-1:]:
            g=g+np.square(x-0.5)-np.cos((x-0.5)*20*np.pi)
        g=g*100
        for i in xrange(self.objnum):
            tmp=1+g
            for x in self.dec[:self.objnum-1-i]:
                tmp=tmp*np.cos(x*np.pi/2)
            if not i==0:
                tmp=tmp*np.sin(self.dec[self.objnum-i]*np.pi/2)
            f.append(tmp)
        self.lastdec=self.dec
        self.obj=f
        return f

class DTLZ5(Model):
    def __init__(self,n=10,m=2):
        self.bottom=[0]*n
        self.top=[1]*n
        self.decnum=n
        self.objnum=m
        self.dec=[0]*n
        self.lastdec=[]
        self.obj=[]
        self.any()

    def getobj(self):

        if self.dec==self.lastdec:
            return self.obj

        f=[]
        g=0
        for x in self.dec[self.objnum-1:]:
            g=g+np.square(x-0.5)
        theta=[np.pi*self.dec[0]/2]
        for x in self.dec[1:self.objnum-1]:
            theta.append((1+2*g*x)*np.pi/(4*(1+g)))
        for i in xrange(self.objnum):
            tmp=1+g
            for x in theta[:self.objnum-1-i]:
                tmp=tmp*np.cos(x*np.pi/2)
            if not i==0:
                tmp=tmp*np.sin(theta[self.objnum-i-1]*np.pi/2)
            f.append(tmp)
        self.lastdec=self.dec
        self.obj=f
        return f

class DTLZ7(Model):
    def __init__(self,n=10,m=2):
        self.bottom=[0]*n
        self.top=[1]*n
        self.decnum=n
        self.objnum=m
        self.dec=[0]*n
        self.lastdec=[]
        self.obj=[]
        self.any()

    def getobj(self):
        if self.dec==self.lastdec:
            return self.obj
        f=[]
        g=1+9/(self.decnum-self.objnum+1)*np.sum(self.dec[self.objnum-1:])
        h=self.objnum
        for i in xrange(self.objnum-1):
            f.append(self.dec[i])
            h=h-f[i]/(1+g)*(1+np.sin(3*np.pi*f[i]))
        f.append((1+g)*h)
        self.lastdec=self.dec
        self.obj=f
        return f

"""
def better_gen(pf_new,pf,rate):
    count=0
    for a in pf:
        for b in pf_new:
            if is_bd(b,a):
                count=count+1
    whole=len(pf)*len(pf_new)
    if count>-int(whole*rate):
        return True
    else:
        return False
"""

"is a binary dominate b? smaller is better"
def is_bd(a,b):
    try:
        obj_a=a.getobj()
    except:
        obj_a=a
    try:
        obj_b=b.getobj()
    except:
        obj_b=b
    if obj_a==obj_b:
        return False
    for i in xrange(a.objnum):
        if obj_b[i]<obj_a[i]:
            return False
    return True

def crossover(a,b,baby):
    while True:
        x=randint(0,len(a.dec))
        baby.dec=list(np.array(a.dec)[:x])+list(np.array(b.dec)[x:])
        if baby.check():
            return baby

def mutate(baby):
    baby.any()
    return baby

"Update pf_best"
def compete(pf_best,pf_new):
    tmp=[]
    for a in pf_new:
        for b in pf_best:
            if is_bd(a,b):
                tmp.append(a)
                pf_best.remove(b)
    if tmp:
        pf_best.extend(tmp)
        return True
    else:
        return False

""
def init(Model,decnum=10,objnum=2,num=10000):
    can=[Model(decnum,objnum) for _ in xrange(num)]
    max=[np.max([c.getobj()[i] for c in can]) for i in range(objnum)]
    min=[np.min([c.getobj()[i] for c in can]) for i in range(objnum)]
    return min,max


def GeneticAlgorithm(Model,decnum=10,objnum=2,the_seed=1,candidates=100,generations=1000,mutation_rate=0.05,lifes=5):
    seed(the_seed)

    can=[Model(decnum,objnum) for _ in xrange(candidates)]

    pf=[]
    for a in can:
        flag=True
        for b in can:
            if is_bd(b,a):
                flag=False
                break
        if flag:
            pf.append(a)
    pf_best=pf[:]
    life=0
    for i in xrange(generations):
        can_new=[]
        for j in xrange(candidates):
            baby=Model()
            pick=np.random.choice(len(pf),2,replace=True)
            crossover(pf[pick[0]],pf[pick[1]],baby)
            if random()<mutation_rate*(2**life):
                mutate(baby)
            can_new.append(baby)
        pf_new=[]
        for a in can:
            flag=True
            for b in can:
                if is_bd(b,a):
                    flag=False
                    break
            if flag:
                pf_new.append(a)
        change=compete(pf_best,pf_new)
        if change:
            life=0
        else:
            life=life+1
        if life==lifes:
            break
        #print("Frontier num: "+str(len(pf_best)))

        can=can_new
        pf=pf_new

    return pf_best


"""
def upminmax(min,max,pf):
    for c in pf:
        for i in xrange(len(min)):
            if min[i]>c.getobj()[i]:
                min[i]=c.getobj()[i]
            elif max[i]<c.getobj()[i]:
                max[i]=c.getobj[i]
    return min,max
"""

if __name__ == '__main__':
    candidates=100
    generations=1000
    mutation_rate=0.05
    lifes=5

    models=[DTLZ1,DTLZ3,DTLZ5,DTLZ7]
    objs=[2,4,6,8]
    decs=[10,20,40]
    hv={}
    for model in models:
        hv[model.__name__]={}
        for objnum in objs:
            hv[model.__name__][objnum]={}
            for decnum in decs:
                hv[model.__name__][objnum][decnum]=[]
                min,max=init(model,decnum=decnum,objnum=objnum,num=100000)
                for the_seed in xrange(20):
                    pf=GeneticAlgorithm(model,decnum=decnum,objnum=objnum,the_seed=the_seed,candidates=candidates,
                                        generations=generations,mutation_rate=mutation_rate,lifes=lifes)
                    #min,max=upminmax(min,max,pf)
                    hv[model.__name__][objnum][decnum].append(hve(pf,min,max,100000))

    with open('hypervolumn.pickle', 'wb') as handle:
        pickle.dump(hv, handle)
    set_trace()
    with open('./data/hypervolumn.pickle', 'wb') as handle:
        pickle.dump(hv, handle)



