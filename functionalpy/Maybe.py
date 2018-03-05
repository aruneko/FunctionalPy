from typing import Generic, TypeVar, Callable

from functionalpy.Monad import Monad

A = TypeVar('A')
B = TypeVar('B')


class Maybe(Monad, Generic[A]):
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
