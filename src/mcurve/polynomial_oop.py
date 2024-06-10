class Polynomial:

    def __init__(self, *argv: list[float]):
        self.__coefficients = []
        for c in argv:
            self.__coefficients.append(c)

    def evaluate(self, x: float) -> tuple[float, list[float]]:
        p = self.__coefficients[-1]
        c = [p]
        for ak in self.__coefficients[-2::-1]:
            p = ak + (p * x)
            c.insert(0, p)
        return c[0], c[1:]

    def __repr__(self):
        buffer = ""
        for c in self.__coefficients:
            buffer += f" {c}"
        return buffer

