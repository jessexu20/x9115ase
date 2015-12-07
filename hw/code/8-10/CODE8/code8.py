from __future__ import print_function, unicode_literals
from __future__ import absolute_import, division
from random import uniform,randint,random,seed
from time import time
import numpy as np
from pdb import set_trace
import pickle

t=10
c=100
ERA_SIZE=20

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
        
    @staticmethod
    def lessThan(a,b):
        return a<b


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
        

def neighbor(s,index,model):
    sn=model()
    sn.copy(s)
    while True:
        sn.dec[index]=uniform(sn.bottom[index],sn.top[index])
        if sn.check(): break
    return sn
    

class o():
  "Anonymous container"
  def __init__(i,**fields) : 
    i.override(fields)
  def override(i,d): i.__dict__.update(d); return i
  def __repr__(i):
    d = i.__dict__
    name = i.__class__.__name__
    return name+'{'+' '.join([':%s %s' % (k,pretty(d[k])) 
                     for k in i.show()])+ '}'
  def show(i):
    return [k for k in sorted(i.__dict__.keys()) 
            if not "_" in k]


def a12(lst1,lst2):
  "how often is x in lst1 more than y in lst2?"
  def loop(t,t1,t2): 
    while t1.j < t1.n and t2.j < t2.n:
      h1 = t1.l[t1.j]
      h2 = t2.l[t2.j]
      h3 = t2.l[t2.j+1] if t2.j+1 < t2.n else None 
      if h1>  h2:
        t1.j  += 1; t1.gt += t2.n - t2.j
      elif h1 == h2:
        if h3 and h1 > h3 :
            t1.gt += t2.n - t2.j  - 1
        t1.j  += 1; t1.eq += 1; t2.eq += 1
      else:
        t2,t1  = t1,t2
    return t.gt*1.0, t.eq*1.0
  #--------------------------
  lst1 = sorted(lst1, reverse=True)
  lst2 = sorted(lst2, reverse=True)
  n1   = len(lst1)
  n2   = len(lst2)
  t1   = o(l=lst1,j=0,eq=0,gt=0,n=n1)
  t2   = o(l=lst2,j=0,eq=0,gt=0,n=n2)
  gt,eq= loop(t1, t1, t2)
  return gt/(n1*n2) + eq/2/(n1*n2)


def simulated_annealing(model):

    def probability(en,e,T):
        return np.exp(-(((en-e)/max(np.abs(en),np.abs(e)))/T**3))
    
    s=model()
    sb=model()
    sb.copy(s)
    kmax=c*t
    linewidth=c
    cur_era=[0]*ERA_SIZE
    prev_era=[0]*ERA_SIZE
    e=0
    life=5
    #for k in range(0,kmax):
    k=0
    while(life!=0):
        T=(kmax+1-k)/kmax
        sn=neighbor(s,randint(0,s.decnum-1),model)
        if k%linewidth==0:
            print(", %4d, : %s, " %(k,sb.dec),end="")
        #if sn.eval()<sb.eval():
        
        if(e==20):
            if a12(cur_era,prev_era)>0.56: #Check this
                life=5
            else:
                life-=1
            prev_era=cur_era
            cur_era=[0]*ERA_SIZE
            e=0
        else:
            cur_era[e]=sn.eval()
            e+=1
        
        if model.lessThan(sn.eval(),sb.eval()):
            sb.copy(sn)
            s.copy(sn)
            print("!",end="")
        elif model.lessThan(sn.eval(),s.eval()):
            s.copy(sn)
            print("+",end="")
        elif probability(sn.eval(),s.eval(),T)>random():
            s.copy(sn)
            print("?",end="")
        else:
            print(".",end="")
        if k%linewidth==linewidth-1:
            print("")
        k+=1
    print("")
    #print("Best solution: %s, " %sb.dec,"f1 and f2: %s, " %sb.getobj(),"steps: %s" %kmax)
    print("Best solution: %s, " %sb.dec,"f1 and f2: %s, " %sb.getobj())
    return True
    
def maxwalksat(model):

    def optc(s_old,which,step):
        sn=model()
        sn.copy(s_old)
        snbest=model()
        snbest.copy(sn)
        dis=(sn.top[which]-sn.bottom[which])/step
        for i in range(-int((s_old.dec[which]-s_old.bottom[which])/dis),int((s_old.top[which]-s_old.dec[which])/dis)+1):
            sn.dec[which]=sn.dec[which]+i*dis
            if not sn.check(): continue
            if sn.eval()<snbest.eval():
                snbest.copy(sn)
        return snbest

    eval=0
    evalx=0
    maxtries=t
    maxchanges=c
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
          
          
def differential_evolution(model):

    def mutate(candidates,f,cr,xbest):
        for i in range(len(candidates)):
            tmp=range(len(candidates))
            tmp.remove(i)
            while True:
                abc=np.random.choice(tmp,3)
                a3=[candidates[tt] for tt in abc]
                xold=candidates[i]
                r=randint(0,xold.decnum-1)
                xnew=model()
                for j in range(xold.decnum):
                    if random()<cr or j==r:
                        xnew.dec[j]=a3[0].dec[j]+f*(a3[1].dec[j]-a3[2].dec[j])
                    else:
                        xnew.dec[j]=xold.dec[j]
                if xnew.check(): break
            if xnew.eval()<xbest.eval():
                xbest.copy(xnew)
                print("!",end="")
            elif xnew.eval()<xold.eval():
                print("+",end="")
            else:
                xnew=xold
                print(".",end="")
            yield xnew


    nb=c
    maxtries=t
    f=0.75
    cr=0.3
    xbest=model()
    candidates=[xbest]
    for i in range(1,nb):
        x=model()
        candidates.append(x)
        if x.eval()<xbest.eval():
            xbest.copy(x)
    for tries in range(maxtries):
        print(", Retries: %2d, : Best solution: %s, " %(tries,xbest.dec),end="")
        candidates=[xnew for xnew in mutate(candidates,f,cr,xbest)]
        print("")
    print("Best solution: %s, " %xbest.dec,"f1 and f2: %s, " %xbest.getobj(),
          "evals: %s * %s" %(nb,maxtries))


    
if __name__ == '__main__':
    model=DTLZ7
    simulated_annealing(DTLZ7)
    #maxwalksat(DTLZ7)
    #differential_evolution(DTLZ7)