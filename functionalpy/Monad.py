from abc import abstractmethod, ABCMeta
from typing import Callable, TypeVar, Generic

from functionalpy.Applicative import Applicative

A = TypeVar('A')
B = TypeVar('B')


class Monad(Applicative, Generic[A], metaclass=ABCMeta):
    @abstractmethod
    def flat_map(self, f):
        # type: (Callable[[A], Monad[B]]) -> Monad[B]
        pass
