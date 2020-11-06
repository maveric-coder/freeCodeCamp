
import numpy as np

def calculate(list):
    if len(list)!=9:
        raise ValueError("List must contain nine numbers.")
    ls=np.array(list).reshape((3,3))
    
    
    ## mean
    mean_z=ls.mean(axis=0)
    mean_o=ls.mean(axis=1)
    mean=ls.mean()
    
    ## Variance
    var_z=ls.var(axis=0)
    var_o=ls.var(axis=1)
    var=ls.var()
    
    ## Standard Deviation
    std_z=ls.std(axis=0)
    std_o=ls.std(axis=1)
    std=ls.std()
    
    ## Max
    max_z=ls.max(axis=0)
    max_o=ls.max(axis=1)
    ma=ls.max()
    
    ## Min
    min_z=ls.min(axis=0)
    min_o=ls.min(axis=1)
    mi=ls.min()
    
    
    ## Sum
    sum_z=ls.sum(axis=0)
    sum_o=ls.sum(axis=1)
    su=ls.sum()
    
    calc= {'mean':[[i for i in mean_z],[i for i in mean_o],mean], 'variance':[[i for i in var_z],[i for i in var_o],var],'standard deviation':[[i for i in std_z],[i for i  in std_o],std],'max':[[i for i in max_z],[i for i in max_o],ma],'min':[[i for i in min_z],[i for i in min_o],mi],'sum':[[i for i  in sum_z],[i for i in sum_o],su]}
    

    return calc
print(calculate([0,1,2,3,4,5,6,7,8]))
