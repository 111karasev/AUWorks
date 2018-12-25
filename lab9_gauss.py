import numpy as np
np.seterr(divide='ignore', invalid='ignore')

arrA = np.array([
    [1.,2.,1.,5.],
    [3.,2.,3.,6.],
    [1.,0.,0.,7.]
])

razmer=3

def gauss(size, arrA):
    for i in range(size):
        arrA[i]=arrA[i]/arrA[i][i]
        for q in range(1+i, size):
            arrA[q]-=arrA[i]*arrA[q][i]
    for i in range(size-1,-1,-1):
        for q in range(i-1, -1, -1):
            arrA[q]-=arrA[i]*arrA[q][i]
    return arrA[:,size]
    
print(gauss(razmer, arrA))
