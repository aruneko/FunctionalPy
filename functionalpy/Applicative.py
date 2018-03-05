from abc import abstractmethod
from typing import TypeVar, Callable

from functionalpy.Functor import Functor

A = TypeVar('A')
B = TypeVar('B')


class Applicative(Functor):
    @abstractmethod
    def ap(self, f):
        # type: (Applicative[Callable[[A], B]]) -> Applicative[B]
        pass
