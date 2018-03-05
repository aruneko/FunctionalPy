from abc import ABC, abstractmethod
from typing import TypeVar, Callable

A = TypeVar('A')
B = TypeVar('B')


class Functor(ABC):
    @abstractmethod
    def map(self, f):
        # type: (Callable[[A], B]) -> Functor[B]
        pass
