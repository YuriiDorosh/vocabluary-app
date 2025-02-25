from typing import Optional
from django.db.models import QuerySet
from src.apps.common.services import BaseService
from src.apps.words.repositories.tags import UserTagsRepository, WordTagsRepository
from src.apps.words.models.tags import UserTag, WordTag
from src.apps.common.pagination import PaginatedResult, PaginationParams


class UserTagsService(BaseService[UserTag]):
    def __init__(self) -> None:
        repository = UserTagsRepository()
        super().__init__(repository)

    def get_all(self, pagination: PaginationParams, **filters) -> PaginatedResult[UserTag]:
        return self.repository.get_all(pagination, **filters)

    def get_by_id(self, obj_id: int) -> Optional[UserTag]:
        return self.repository.get_by_id(obj_id)

    def create(self, **kwargs) -> UserTag:
        return self.repository.create(**kwargs)

    def update(self, obj_id: int, **kwargs) -> Optional[UserTag]:
        return self.repository.update(obj_id, **kwargs)

    def delete(self, obj_id: int) -> bool:
        return self.repository.delete(obj_id)
    

class WordTagsService(BaseService[WordTag]):
    def __init__(self) -> None:
        repository = WordTagsRepository()
        super().__init__(repository)

    def get_all(self, pagination: PaginationParams, **filters) -> PaginatedResult[WordTag]:
        return self.repository.get_all(pagination, **filters)

    def get_by_id(self, obj_id: int) -> Optional[WordTag]:
        return self.repository.get_by_id(obj_id)

    def create(self, **kwargs) -> WordTag:
        return self.repository.create(**kwargs)

    def update(self, obj_id: int, **kwargs) -> Optional[WordTag]:
        return self.repository.update(obj_id, **kwargs)

    def delete(self, obj_id: int) -> bool:
        return self.repository.delete(obj_id)