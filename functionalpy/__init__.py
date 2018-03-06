from abc import ABCMeta
from functools import reduce
from typing import Callable, TypeVar, Generic, Tuple, Iterable

from functionalpy.Foldable import Foldable
from functionalpy.Monad import Monad

A = TypeVar('A')
B = TypeVar('B')
C = TypeVar('C')


class Seq(list, Monad, Foldable, Generic[A]):
    def __init__(self, *values) -> None:
        super().__init__(values)

    @staticmethod
    def to_seq(iterable):
        # type: (Iterable[A]) -> Seq[A]
        return Seq(*iterable)

    def map(self, f):
        # type: (Callable[[A], B]) -> Seq[B]
        return Seq(*map(f, self))

    def ap(self, fs):
        # type: (Seq[Callable[[A], B]]) -> Seq[B]
        return Seq(*[f(x) for f in fs for x in self])

    def flat_map(self, f):
        # type: (Callable[[A], Seq[B]]) -> Seq[B]
        return Seq(*[y for x in self for y in f(x)])

    def flatten(self):
        # type: () -> Seq[A]
        return Seq(*[i for out in self for i in out])

    def fold(self, f, x):
        # type: (Callable[[B, A], B], B) -> B
        return reduce(f, self, x)

    def fold1(self, f):
        # type: (Callable[[A, A], A]) -> A
        return reduce(f, self)

    def filter(self, f):
        # type: (Callable[[A], bool]) -> Seq[A]
        return Seq(*filter(f, self))

    def zip(self, xs):
        # type: (Seq[B]) -> Seq[Tuple[A, B]]
        return Seq(*zip(self, xs))

    def zip_with(self, f, xs):
        # type: (Callable[[A, B], C], Seq[B]) -> Seq[C]
        return Seq(*map(f, self, xs))

    def unzip(self):
        # type: () -> Tuple[Seq[A], Seq[B]]
        return self.map(lambda x: x[0]), self.map(lambda x: x[1])

    def sort(self):
        # type: () -> Seq[A]
        return Seq(*sorted(self))

    def reverse(self):
        # type: () -> Seq[A]
        return Seq(*reversed(self))

    def for_each(self, f):
        # type: (Callable[[A], None]) -> None
        for x in self:
            f(x)

    def head(self):
        # type: () -> A
        return self[0]

    def tail(self):
        # type: () -> Seq[A]
        return Seq(*self[1:])

    def last(self):
        # type: () -> A
        return self[-1]

    def init(self):
        # type: () -> Seq[A]
        return Seq(*self[:-1])


class Maybe(Monad, Generic[A], metaclass=ABCMeta):
    def __init__(self, x: A) -> None:
        self.value = x


class _Nothing(Maybe, Generic[A]):
    def __init__(self, x: A) -> None:
        super().__init__(x)

    def __repr__(self) -> str:
        return 'Nothing'

    def map(self, f):
        # type: (Callable[[A], B]) -> Maybe[B]
        return self

    def ap(self, f):
        # type: (Maybe[Callable[[A], B]]) -> Maybe[B]
        return self

    def flat_map(self, f):
        # type: (Callable[[A], Maybe[B]]) -> Maybe[B]
        return self

    def get_or_else(self, x):
        # type: (A) -> A
        return x


Nothing = _Nothing(None)


class Just(Maybe, Generic[A]):
    def __init__(self, x: A) -> None:
        super().__init__(x)

    def __repr__(self) -> str:
        return f'Just({self.value})'

    def map(self, f):
        # type: (Callable[[A], B]) -> Maybe[B]
        return Just(f(self.value))

    def ap(self, f):
        # type: (Maybe[Callable[[A], B]]) -> Maybe[B]
        if f is Nothing:
            return Nothing
        else:
            return Just(f.value(self.value))

    def flat_map(self, f):
        # type: (Callable[[A], Maybe[B]]) -> Maybe[B]
        result = f(self.value)
        if result is Nothing:
            return Nothing
        else:
            return result

    def get_or_else(self, _):
        # type: (A) -> A
        return self.value
