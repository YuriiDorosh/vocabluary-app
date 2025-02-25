from typing import Optional
from django.db.models import QuerySet
from src.apps.common.services import BaseService
from src.apps.words.repositories.word_images import WordImagesRepository
from src.apps.words.models.word_images import WordImage
from src.apps.common.pagination import PaginatedResult, PaginationParams


class WordImagesService(BaseService[WordImage]):
    def __init__(self) -> None:
        repository = WordImagesRepository()
        super().__init__(repository)

    def get_all(self, pagination: PaginationParams, **filters) -> PaginatedResult[WordImage]:
        return self.repository.get_all(pagination, **filters)

    def get_by_id(self, obj_id: int) -> Optional[WordImage]:
        return self.repository.get_by_id(obj_id)

    def create(self, **kwargs) -> WordImage:
        return self.repository.create(**kwargs)

    def update(self, obj_id: int, **kwargs) -> Optional[WordImage]:
        return self.repository.update(obj_id, **kwargs)

    def delete(self, obj_id: int) -> bool:
        return self.repository.delete(obj_id)