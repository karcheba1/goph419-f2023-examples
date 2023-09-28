def exp(x):
    """Compute values of the exponential function for real-valued scalar input.

    Parameters
    ----------
    x : float_like
        The argument of the exponential function

    Returns
    -------
    float
        The value of the exponential function at x
    """
    x = float(x)
    tol = 1.0e-16
    eps_a = 2 * tol
    sum = 0.0
    k = 0
    fact_k = 1
    while eps_a > tol:
        term = x ** k / fact_k
        sum += term
        eps_a = abs(term / sum)
        k += 1
        fact_k *= k
    return sum


def sin(x):
    """Compute values of the sine function for real-valued scalar input.

    Parameters
    ----------
    x : float_like
        The argument of the sine function

    Returns
    -------
    float
        The value of the sine function at x
    """
    x = float(x)
    tol = 1.0e-16
    eps_a = 2 * tol
    sum = 0.0
    k = 0
    fact_k = 1
    while eps_a > tol:
        term = (-1) ** k * x ** (2 * k + 1) / fact_k
        sum += term
        eps_a = abs(term / sum)
        k += 1
        fact_k *= (2 * k) * (2 * k + 1)
    return sum
