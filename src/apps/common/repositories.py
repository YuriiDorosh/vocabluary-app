from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, Optional
from django.db.models import QuerySet
from src.apps.common.pagination import PaginationParams, PaginatedResult

T = TypeVar("T")


class AbstractORMRepository(ABC, Generic[T]):
    @abstractmethod
    def get_all(self, pagination: PaginationParams, **filters) -> PaginatedResult[T]:
        pass

    @abstractmethod
    def get_by_id(self, obj_id: int) -> Optional[T]:
        pass

    @abstractmethod
    def create(self, **kwargs) -> T:
        pass

    @abstractmethod
    def update(self, obj_id: int, **kwargs) -> Optional[T]:
        pass

    @abstractmethod
    def delete(self, obj_id: int) -> bool:
        pass
