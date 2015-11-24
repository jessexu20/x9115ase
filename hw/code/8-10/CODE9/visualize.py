from __future__ import print_function, unicode_literals
from __future__ import absolute_import, division
from random import uniform,randint,random,seed
import numpy as np
from pdb import set_trace
import pickle
import pandas as pd

def iqr(lst):
  q75,q25=np.percentile(lst, [75 ,25])
  return q75-q25

if __name__ == '__main__':
    candidates=100
    generations=1000
    mutation_rate=0.05
    life=5

    models=['DTLZ1','DTLZ3','DTLZ5','DTLZ7']
    objs=[2,4,6,8]
    decs=[10,20,40]

    with open('./data/hypervolumn.pickle', 'rb') as handle:
        hv=pickle.load(handle)

    hv_st={}
    for model in models:
        hv_st[model]={}
        tmp=[]
        for objnum in objs:
            hv_st[model][objnum]={}
            tmp2=[]
            for decnum in decs:
                hv_st[model][objnum][decnum]=[]
                hv_st[model][objnum][decnum].append(np.median(hv[model][objnum][decnum]))
                hv_st[model][objnum][decnum].append(iqr(hv[model][objnum][decnum]))
                tmp2.append(str(np.median(hv[model][objnum][decnum]))+u"\u00b1"+str(iqr(hv[model][objnum][decnum])))
            tmp.append(tmp2)


        print("model: "+str(model))

        print(pd.DataFrame(data = tmp, columns=decs,index=objs))