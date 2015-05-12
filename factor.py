import numpy as np

def LU(A):
    r"""Factor a square matrix by Gaussian elimination.

        The argument A should be a square matrix (an m-by-m numpy array).

        The outputs L and U are also m-by-m.  L is lower-triangular with
        unit diagonal entries and U is strictly upper-triangular.

        This implementation does not use pivoting and can be unstable
        for moderately large matrices, due to amplification of roundoff errors.
        See, e.g., Lectures 20-22 of the book by Trefethen & Bau for a discussion.

        Example::

            >>> import factor
            >>> import numpy as np
            >>> A = np.array([[2.,1.,1.,0.],[4.,3.,3.,1.],[8.,7.,9.,5.],[6.,7.,9.,8.]])
            >>> print A
            [[ 2.  1.  1.  0.]
             [ 4.  3.  3.  1.]
             [ 8.  7.  9.  5.]
             [ 6.  7.  9.  8.]]
            >>> L, U = factor.LU(A)
            >>> print L
            [[ 1.  0.  0.  0.]
             [ 2.  1.  0.  0.]
             [ 4.  3.  1.  0.]
             [ 3.  4.  1.  1.]]
            >>> print U
            [[ 2.  1.  1.  0.]
             [ 0.  1.  1.  1.]
             [ 0.  0.  2.  2.]
             [ 0.  0.  0.  2.]]
    """
    m = A.shape[0]
    U = A.copy()
    L = np.eye( m )
    for j in range(m):
        for i in range(j+1,m):
            L[i,j] =  U[i,j]/U[j,j]
            U[i,:] -= L[i,j]*U[j,:]

    return L, U


if __name__ == "__main__":
    import doctest
    doctest.testmod()
