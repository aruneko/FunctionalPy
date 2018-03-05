from abc import abstractmethod, ABCMeta
from typing import TypeVar, Callable, Generic

A = TypeVar('A')
B = TypeVar('B')


class Functor(Generic[A], metaclass=ABCMeta):
    @abstractmethod
    def map(self, f):
        # type: (Callable[[A], B]) -> Functor[B]
        pass
