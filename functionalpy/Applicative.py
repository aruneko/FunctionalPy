from abc import abstractmethod, ABCMeta
from typing import TypeVar, Callable, Generic

from functionalpy.Functor import Functor

A = TypeVar('A')
B = TypeVar('B')


class Applicative(Functor, Generic[A], metaclass=ABCMeta):
    @abstractmethod
    def ap(self, f):
        # type: (Applicative[Callable[[A], B]]) -> Applicative[B]
        pass
