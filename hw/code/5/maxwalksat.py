from __future__ import print_function, unicode_literals
from __future__ import absolute_import, division
from random import uniform,randint,random
from pdb import set_trace


xmax=[10,10,5,6,5,10]
xmin=[0,0,1,0,1,0]


def osyczka2(x):
    f1=-(25*(x[0]-2)**2+(x[1]-2)**2+((x[2]-1)**2)*(x[3]-4)**2+(x[4]-1)**2)
    f2=x[0]**2+x[1]**2+x[2]**2+x[3]**2+x[4]**2+x[5]**2
    return f1+f2

def constraints(x):
    g=[0,0,0,0,0,0]
    g[0]=x[0]+x[1]-2
    g[1]=6-x[0]-x[1]
    g[2]=2-x[1]+x[0]
    g[3]=2-x[0]+3*x[1]
    g[4]=4-x[3]-(x[2]-3)**2
    g[5]=(x[4]-3)**3+x[5]-4
    for i in range(0,6):
        if x[i]<xmin[i] or x[i]>xmax[i] or g[i]<0:
            return False
    return True

def generate_randx():
    x=[]
    for i in range(0,6):
        x.append(uniform(xmin[i],xmax[i]))
    return x

def optc(x,cc,step):
    xc=x[:]
    xcbest=x[:]
    dis=(xmax[cc]-xmin[cc])/step
    for i in range(-int((x[cc]-xmin[cc])/dis),int((xmax[cc]-x[cc])/dis)+1):
        xc[cc]=x[cc]+i*dis
        if not constraints(xc): continue
        if osyczka2(xcbest)<osyczka2(xc):
            xcbest=xc[:]
    return xcbest


def maxwalksat(maxtries,maxchanges,p,threshold):
    eval=0
    for i in range(0,maxtries):

        while True:
            x=generate_randx()
            if constraints(x): break

        if i==0: xbest=x[:]
        for j in range(0,maxchanges):
            if j==0:
                print(", %4d, : %s, " %(eval,xbest),end="")
            eval+=1
            if osyczka2(x)>threshold:
                return {'solution': x,'evals': eval}
            c=randint(0,5)
            if p<random():
                while True:
                    x[c]=uniform(xmin[c],xmax[c])
                    if constraints(x): break
                if osyczka2(xbest)<osyczka2(x):
                    xbest=x[:]
                    print("!",end="")
                else:
                    print("?",end="")
            else:
                x=optc(x,c,step)
                if osyczka2(xbest)<osyczka2(x):
                    xbest=x[:]
                    print("!",end="")
                else:
                    print("+",end="")
        print("")


    return {'solution': xbest,'evals': eval}


if __name__ == '__main__':
    maxtries=20
    maxchanges=100
    p=0.5
    threshold=1000000
    step=10
    results=maxwalksat(maxtries,maxchanges,p,threshold)
    print("")
    print("Best solution: %s, " %results['solution'],"f1+f2 (maximization): %s, " %osyczka2(results['solution']),"step * eval: %s * %s" %(step,results['evals']))