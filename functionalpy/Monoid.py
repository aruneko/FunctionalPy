from abc import ABCMeta, abstractmethod
from typing import TypeVar, Generic, List

A = TypeVar('A')


class Monoid(Generic[A], metaclass=ABCMeta):
    def __add__(self, other):
        # type: (Monoid[A]) -> Monoid[A]
        return self.append(other)

    @staticmethod
    def mempty():
        # type: () -> Monoid[A]
        raise NotImplementedError

    @abstractmethod
    def append(self, other):
        # type: (Monoid[A]) -> Monoid[A]
        pass


def concat(monoid_list):
    # type: (List[Monoid[A]]) -> Monoid[A]
    acc = monoid_list[0].mempty()
    for x in monoid_list:
        acc += x
    return acc
