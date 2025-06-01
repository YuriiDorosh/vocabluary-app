from django.db.models import QuerySet
from typing import Optional
from src.apps.common.repositories import AbstractORMRepository
from src.apps.words.models.categories import UserCategory, WordCategory
from src.apps.common.pagination import PaginatedResult, PaginationParams


class CategoriesRepository(AbstractORMRepository[UserCategory]):
    def get_all(self, pagination: PaginationParams, **filters) -> PaginatedResult[UserCategory]:
        qs = UserCategory.objects.all()
        if filters:
            qs = qs.filter(**filters)
        total_count = qs.count()
        start = (pagination.page - 1) * pagination.page_size
        end = start + pagination.page_size
        items = list(qs[start:end])
        return PaginatedResult(
            items=items,
            total_count=total_count,
            page=pagination.page,
            page_size=pagination.page_size,
        )
    
    def get_by_id(self, obj_id: int) -> Optional[UserCategory]:
        return UserCategory.objects.get(id=obj_id)
    
    def create(self, **kwargs) -> UserCategory:
        return UserCategory.objects.create(**kwargs)
    
    def update(self, obj_id: int, **kwargs) -> Optional[UserCategory]:
        category = UserCategory.objects.get(id=obj_id)
        for key, value in kwargs.items():
            setattr(category, key, value)
        category.save()
        return category
    
    def delete(self, obj_id: int) -> bool:
        category = UserCategory.objects.get(id=obj_id)
        category.delete()
        return True
    

class WordCategoriesRepository(AbstractORMRepository[WordCategory]):
    def get_all(self, pagination: PaginationParams, **filters) -> PaginatedResult[WordCategory]:
        qs = WordCategory.objects.all()
        if filters:
            qs = qs.filter(**filters)
        total_count = qs.count()
        start = (pagination.page - 1) * pagination.page_size
        end = start + pagination.page_size
        items = list(qs[start:end])
        return PaginatedResult(
            items=items,
            total_count=total_count,
            page=pagination.page,
            page_size=pagination.page_size,
        )
    
    def get_by_id(self, obj_id: int) -> Optional[WordCategory]:
        return WordCategory.objects.get(id=obj_id)
    
    def create(self, **kwargs) -> WordCategory:
        return WordCategory.objects.create(**kwargs)
    
    def update(self, obj_id: int, **kwargs) -> Optional[WordCategory]:
        category = WordCategory.objects.get(id=obj_id)
        for key, value in kwargs.items():
            setattr(category, key, value)
        category.save()
        return category
    
    def delete(self, obj_id: int) -> bool:
        category = WordCategory.objects.get(id=obj_id)
        category.delete()
        return True