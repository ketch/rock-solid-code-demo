import numpy as np
import factor

def test():
    A = np.random.rand(3,3)
    L, U = factor.LU(A)
    assert np.allclose(A, np.dot(L,U))

