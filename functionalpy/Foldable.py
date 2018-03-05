from abc import ABC, abstractmethod
from typing import Callable, TypeVar

A = TypeVar('A')
B = TypeVar('B')


class Foldable(ABC):
    @abstractmethod
    def fold(self, f, x):
        # type: (Callable[[B, A], B], B) -> B
        pass

    @abstractmethod
    def fold1(self, f):
        # type: (Callable[[A], A]) -> A
        pass
