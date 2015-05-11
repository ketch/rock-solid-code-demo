import numpy as np

def LU(A):
    m = A.shape[0]
    U = A.copy()
    L = np.eye( m )
    for j in range(m):
        for i in range(j+1,m):
            L[i,j] =  U[i,j]/U[j,j]
            U[i,:] -= L[i,j]*U[j,:]

    return L, U
