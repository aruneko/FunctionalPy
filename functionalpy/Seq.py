from functools import reduce
from typing import Callable, TypeVar, Generic

from functionalpy.Foldable import Foldable
from functionalpy.Monad import Monad

A = TypeVar('A')
B = TypeVar('B')


class Seq(list, Monad, Foldable, Generic[A]):
    def __init__(self, *values) -> None:
        super().__init__(values)

    def map(self, f):
        # type: (Callable[[A], B]) -> Seq[B]
        return Seq(*map(f, self))

    def ap(self, fs):
        # type: (Seq[Callable[[A], B]]) -> Seq[B]
        return Seq(*[f(x) for f in fs for x in self])

    def flat_map(self, f):
        # type: (Callable[[A], Seq[B]]) -> Seq[B]
        return Seq(*[y for x in self for y in f(x)])

    def fold(self, f, x):
        # type: (Callable[[B, A], B], B) -> B
        return reduce(f, self, x)

    def fold1(self, f):
        # type: (Callable[[A], A]) -> A
        return reduce(f, self)

    def filter(self, f):
        # type: (Callable[[A], bool]) -> Seq[A]
        return Seq(*filter(f, self))
