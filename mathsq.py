import math
from typing import Union


class MathSQ:
    def __init__(
        self,
        a1: float,
        d: float,
        ln: int = 1
    ):
        self.a1 = a1
        self.d = d
        self.ln = ln

    def n(self, __n: int):
        return self.a1 + (__n - 1) * self.d

    def n_of(self, __v: float):
        return (__v - self.a1) / self.d + 1

    def setln(self, __ln: int) -> "MathSQ":
        self.ln = __ln
        return self

    def mid_n(self) -> float:
        return (self.ln + 1) / 2

    def mid(self) -> float:
        return (self.a1 + self.n(self.ln)) / 2

    @property
    def M(self) -> float:
        return self.mid()

    def has_mid(self) -> bool:
        return not self.ln % 2

    def sum(self, __n: int) -> float:
        return self.mid() * self.ln

    @property
    def S(self) -> float:
        return self.sum(self.ln)

    # '+'
    def __add__(self, __other: Union["MathSQ", float]) -> "MathSQ":
        if isinstance(__other, (float, int)):
            return MathSQ(self.a1 + __other, self.d, self.ln)
            
        else:
            assert __other.ln == self.ln, "Length unmatch"
            return MathSQ(self.a1 + __other.a1, self.d + __other.d, self.ln)

    # '-'
    def __sub__(self, __other: Union["MathSQ", float]) -> "MathSQ":
        return self.__add__(
            __other * -1
        )

    # '*'
    def __mul__(self, __other: float) -> "MathSQ":
        return MathSQ(self.a1 * __other, self.d * __other, self.ln)

    def where0(self) -> int:
        if self.a1 == 0:
            return 1

        assert (self.a1 > 0 and self.d < 0) or (self.a1 < 0 and self.d > 0)
        return math.ceil(
            self.a1 / -self.d + 1
            if self.a1 > 0
            else self.a1 / -self.d
        )

    @staticmethod
    def from_n_assignment(
        *,
        n: int,
        value: float,
        d: float,
        ln: int = 1
    ):
        a1 = value - (n - 1) * d
        return MathSQ(a1, d, ln)
