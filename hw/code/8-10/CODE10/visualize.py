from __future__ import print_function
from __future__ import absolute_import, division
from random import uniform,randint,random,seed
import numpy as np
from pdb import set_trace
import pickle
import pandas as pd
from sk import rdivDemo


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
    istune=['tuned','untuned']

    with open('./data/hypervolumn.pickle', 'rb') as handle:
        hv=pickle.load(handle)



    hv_st={}
    for model in models:
        hv_st[model]={}
        tmp=[]
        col=[]
        for objnum in objs:
            hv_st[model][objnum]={}
            for tune in istune:
                tmp2=[]
                for decnum in decs:
                    hv_st[model][objnum][decnum]=[]
                    hv_st[model][objnum][decnum].append(np.median(hv[model][objnum][decnum][tune]))
                    hv_st[model][objnum][decnum].append(iqr(hv[model][objnum][decnum][tune]))
                    tmp2.append(str(np.median(hv[model][objnum][decnum][tune]))+u"\u00b1"+str(iqr(hv[model][objnum][decnum][tune])))
                tmp.append(tmp2)
                col.append(str(objnum)+"_"+tune)


        print("model: "+str(model))

        print(pd.DataFrame(data = tmp, columns=decs ,index=col))
        #print(pd.DataFrame.from_dict(hv_st[model]))

    Better={}
    for model in models:
        Better[model]=[]
        for objnum in objs:
            tmp=[]
            for decnum in decs:
                isbetter=[["untuned"]+hv[model][objnum][decnum]['untuned']]
                isbetter.append(["tuned"]+hv[model][objnum][decnum]['tuned'])
                ranks=rdivDemo(isbetter)
                tmp.append(ranks[0][0]!=ranks[1][0])
            Better[model].append(tmp)

        print("model: "+str(model))
        print(pd.DataFrame(data = Better[model], columns=decs ,index=objs))



