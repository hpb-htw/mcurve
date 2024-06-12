from typing import Sequence


def evaluate(polynomial: Sequence[float], x: float) -> tuple[float, list[float]]:    
    """Evaluate the polynomial !$p(x) = a_0 + a_1x + a_2x2 + ... + a_nx^n$! by the given !$x_0 = x$!
    :param polynomial: coefficients of !$p$!, less significant to most significant
    :param x:
    :return: Pair of (value of polynomial by given !$x_0 = x$!, and the polynomial !$c(x)$!)
    !$c(x) = c_0 + c_1x + c_2x^2 + c_{n-1}x^{n-1}$!, so that !$p(x) = (x - x_0)\\cdot c(x) + p(x_0)$!.
    """
    p = polynomial[-1]
    c = [p]
    for ak in polynomial[-2::-1]:
        p = ak + (p * x)
        c.insert(0, p)
    return c[0], c[1:]

