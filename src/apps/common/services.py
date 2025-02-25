from typing import Generic, TypeVar, Optional
from django.db.models import QuerySet
from src.apps.common.repositories import AbstractORMRepository
from src.apps.common.pagination import PaginationParams, PaginatedResult

T = TypeVar("T")

class BaseService(Generic[T]):
    def __init__(self, repository: AbstractORMRepository[T]) -> None:
        self.repository = repository

    def get_all(self) -> QuerySet[T]:
        return self.repository.get_all()

    def get_all(self, pagination: PaginationParams, **filters) -> PaginatedResult[T]:
        return self.repository.get_all(**filters)

    def create(self, **kwargs) -> T:
        return self.repository.create(**kwargs)

    def update(self, obj_id: int, **kwargs) -> Optional[T]:
        return self.repository.update(obj_id, **kwargs)

    def delete(self, obj_id: int) -> bool:
        return self.repository.delete(obj_id)
