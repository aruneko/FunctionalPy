from abc import abstractmethod
from typing import Callable, TypeVar, Generic

from functionalpy.Applicative import Applicative

A = TypeVar('A')
B = TypeVar('B')


class Monad(Applicative, Generic[A]):
    @abstractmethod
    def flat_map(self, f):
        # type: (Callable[[A], Monad[B]]) -> Monad[B]
        pass
