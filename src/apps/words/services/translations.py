from typing import Optional
from django.db.models import QuerySet
from src.apps.common.services import BaseService
from src.apps.words.repositories.translations import TranslationsRepository
from src.apps.words.models.translations import WordTranslation
from src.apps.common.pagination import PaginatedResult, PaginationParams


class WordTranslationsService(BaseService[WordTranslation]):
    def __init__(self) -> None:
        repository = TranslationsRepository()
        super().__init__(repository)

    def get_all(self, pagination: PaginationParams, **filters) -> PaginatedResult[WordTranslation]:
        return self.repository.get_all(pagination, **filters)

    def get_by_id(self, obj_id: int) -> Optional[WordTranslation]:
        return self.repository.get_by_id(obj_id)

    def create(self, **kwargs) -> WordTranslation:
        return self.repository.create(**kwargs)

    def update(self, obj_id: int, **kwargs) -> Optional[WordTranslation]:
        return self.repository.update(obj_id, **kwargs)

    def delete(self, obj_id: int) -> bool:
        return self.repository.delete(obj_id)