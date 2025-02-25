from typing import Optional
from django.db.models import QuerySet
from src.apps.common.services import BaseService
from src.apps.words.repositories.words import WordsRepository
from src.apps.words.models.words import Word
from src.apps.common.pagination import PaginatedResult, PaginationParams


class WordsService(BaseService[Word]):
    def __init__(self) -> None:
        repository = WordsRepository()
        super().__init__(repository)

    def get_all(self, pagination: PaginationParams, **filters) -> PaginatedResult[Word]:
        return self.repository.get_all(pagination, **filters)

    def get_by_id(self, obj_id: int) -> Optional[Word]:
        return self.repository.get_by_id(obj_id)

    def create(self, **kwargs) -> Word:
        return self.repository.create(**kwargs)

    def update(self, obj_id: int, **kwargs) -> Optional[Word]:
        return self.repository.update(obj_id, **kwargs)

    def delete(self, obj_id: int) -> bool:
        return self.repository.delete(obj_id)