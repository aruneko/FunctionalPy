from abc import ABC, abstractmethod
from typing import TypeVar, Callable, Generic

A = TypeVar('A')
B = TypeVar('B')


class Functor(ABC, Generic[A]):
    @abstractmethod
    def map(self, f):
        # type: (Callable[[A], B]) -> Functor[B]
        pass
