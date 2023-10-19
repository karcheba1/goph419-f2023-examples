import numpy as np


def solve(a, b):
    """Solve a linear system using Gauss elimination.

    Parameters
    ----------
    a : numpy.ndarray, shape=(M,M)
        The coefficient matrix
    b : numpy.ndarray, shape=(M,)
        The dependent variable values
    """
    a = np.array(a, dtype=float)
    b = np.array(b, dtype=float)
    m = len(a)
    ndim = len(a.shape)
    if ndim != 2:
        raise ValueError(f"A has {ndim} dimensions"
                         + ", should be 2")
    if a.shape[1] != m:
        raise ValueError(f"A has {m} rows and {a.shape[1]} cols"
                         + ", should be square")
    ndimb = len(b.shape)
    if ndimb != 1:
        raise ValueError(f"b has {ndimb} dimensions"
                         + ", should be 1D")
    if len(b) != m:
        raise ValueError(f"A has {m} rows, b has {len(b)} values"
                         + ", dimensions incompatible")
    aug = np.hstack([a, np.reshape(b, (m, 1))])
