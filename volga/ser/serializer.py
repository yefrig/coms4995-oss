from abc import abstractmethod
from typing import Protocol, TypeVar, Generator, Mapping


class Serializer(Protocol):
    @abstractmethod
    def __serialize_bool__(self, value: bool) -> None:
        ...

    @abstractmethod
    def __serialize_int__(self, value: int) -> None:
        ...

    @abstractmethod
    def __serialize_float__(self, value: float) -> None:
        ...

    _T = TypeVar('_T')

    @abstractmethod
    def __serialize_seq__(self, seq: Generator[_T, None, None]) -> None:
        ...

    _K = TypeVar('_K')
    _V = TypeVar('_V')

    @abstractmethod
    def __serialize_map__(self, map: Mapping[_K, _V]) -> None:
        ...

    @abstractmethod
    def __serialize_none__(self) -> None:
        ...