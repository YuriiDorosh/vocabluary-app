from typing import Optional
from django.db.models import QuerySet
from src.apps.common.services import BaseService
from src.apps.words.repositories.examples import ExamplesRepository
from src.apps.words.models.examples import WordExample
from src.apps.common.pagination import PaginatedResult, PaginationParams


class WordExamplesService(BaseService[WordExample]):
    def __init__(self) -> None:
        repository = ExamplesRepository()
        super().__init__(repository)

    def get_all(self, pagination: PaginationParams, **filters) -> PaginatedResult[WordExample]:
        return self.repository.get_all(pagination, **filters)

    def get_by_id(self, obj_id: int) -> Optional[WordExample]:
        return self.repository.get_by_id(obj_id)

    def create(self, **kwargs) -> WordExample:
        return self.repository.create(**kwargs)

    def update(self, obj_id: int, **kwargs) -> Optional[WordExample]:
        return self.repository.update(obj_id, **kwargs)

    def delete(self, obj_id: int) -> bool:
        return self.repository.delete(obj_id)