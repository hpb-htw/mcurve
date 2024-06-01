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


def _lineal_polynome(polynom: Sequence[float]) -> str:
    c = polynom[1]
    first_term = f"{-c}" if c < 0 else f" + {c}"
    return f"{polynom[0]} {first_term}"


def to_string(polynomial: Sequence[float], var_name:str = "x") -> str:
    if len(polynomial) == 1:
        return _constant_polynome(polynomial, var_name)
    if len(polynomial) == 2:
        return _lineal_polynome(polynomial, var_name)
    else:
        start = 0
        while polynomial[start] == 0:  # strip zero coefficients
            start += 1
        if start == 0:  # p[0] is significant p[1] may be 0, 1, or else
            term = "p[0] + p[1]x" # todo
        elif start == 1:
            term = "p[1]x"
        else:
            term = "p[2]x^2"
        start = start+1
        for exp, coefficient in enumerate(polynomial[start:], start=start):
            if coefficient != 0: # only eliminate term with exact 0 coefficient
                c = f"- {-coefficient}" if coefficient < 0 else f"+ {coefficient}"
                var = ""
                if exp > 0:
                    var = f"{var_name}^{exp}" if exp > 1 else f"{var_name}"
                term = f"{term} {c}{var}"
        return term

