from dataclasses import dataclass
from typing import Generic, List, TypeVar

T = TypeVar("T")

@dataclass
class PaginationParams:
    page: int = 1
    page_size: int = 10

@dataclass
class PaginatedResult(Generic[T]):
    items: List[T]
    total_count: int
    page: int
    page_size: int
