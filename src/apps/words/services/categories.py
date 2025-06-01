from typing import Optional
from django.db.models import QuerySet
from src.apps.common.services import BaseService
from src.apps.words.repositories.categories import CategoriesRepository, WordCategoriesRepository
from src.apps.words.models.categories import UserCategory, WordCategory
from src.apps.common.pagination import PaginatedResult, PaginationParams


class WordCategoryService(BaseService[WordCategory]):
    def __init__(self) -> None:
        repository = WordCategoriesRepository()
        super().__init__(repository)

    def get_all(self, pagination: PaginationParams, **filters) -> PaginatedResult[WordCategory]:
        return self.repository.get_all(pagination, **filters)

    def get_by_id(self, obj_id: int) -> Optional[WordCategory]:
        return self.repository.get_by_id(obj_id)

    def create(self, **kwargs) -> WordCategory:
        return self.repository.create(**kwargs)

    def update(self, obj_id: int, **kwargs) -> Optional[WordCategory]:
        return self.repository.update(obj_id, **kwargs)

    def delete(self, obj_id: int) -> bool:
        return self.repository.delete(obj_id)
    
class UserCategoryService(BaseService[UserCategory]):
    def __init__(self) -> None:
        repository = CategoriesRepository()
        super().__init__(repository)

    def get_all(self, pagination: PaginationParams, **filters) -> PaginatedResult[UserCategory]:
        return self.repository.get_all(pagination, **filters)

    def get_by_id(self, obj_id: int) -> Optional[UserCategory]:
        return self.repository.get_by_id(obj_id)

    def create(self, **kwargs) -> UserCategory:
        return self.repository.create(**kwargs)

    def update(self, obj_id: int, **kwargs) -> Optional[UserCategory]:
        return self.repository.update(obj_id, **kwargs)

    def delete(self, obj_id: int) -> bool:
        return self.repository.delete(obj_id)