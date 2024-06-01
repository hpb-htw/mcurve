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


def _constant_polynome(polynome: Sequence[float]) -> str:
    return f"{polynome[0]}"


def _get_start_coefficient(c: float) -> str:
    if c == 1:
        return ""
    elif c == -1:
        return "-"
    else:
        return f"{c}"


def _get_free_coefficient(c: float) -> str:
    if c > 0:
        return f"+ {c}"
    else:
        return f"- {-c}"


def _lineal_polynome(polynom: Sequence[float], var_name: str) -> str:
    c = polynom[1]
    first_term = _get_start_coefficient(c)
    term = f"{first_term}{var_name}"
    c = polynom[0]
    if c != 0:
        last_term = _get_free_coefficient(c)
        term = f"{term} {last_term}"
    return term


def _get_middle_coefficient(c: float) -> str:
    if c == 1:
        return "+ "
    if c == -1:
        return "- "
    return f"- {-c}" if c < 0 else f"+ {c}"


def to_string(polynomial: Sequence[float], var_name:str = "x") -> str:
    if len(polynomial) == 1:
        return _constant_polynome(polynomial)
    if len(polynomial) == 2:
        return _lineal_polynome(polynomial, var_name)
    else:
        p_degree = len(polynomial) - 1
        first_term = _get_start_coefficient(polynomial[-1])
        term = f"{first_term}{var_name}^{p_degree}"
        for idx, coe in enumerate(polynomial[-2:1:-1], start=1):
            if coe != 0:
                mid_term = _get_middle_coefficient(coe)
                exp = p_degree - idx
                term = f"{term} {mid_term}{var_name}^{exp}"
        if polynomial[1] != 0:
            mid_term = _get_middle_coefficient(polynomial[1])
            term = f"{term} {mid_term}{var_name}"
        if polynomial[0] != 0:
            last_term = _get_free_coefficient(polynomial[0])
            term = f"{term} {last_term}"
        return term

