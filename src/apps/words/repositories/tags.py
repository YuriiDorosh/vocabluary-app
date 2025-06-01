from django.db.models import QuerySet
from typing import Optional
from src.apps.common.repositories import AbstractORMRepository
from src.apps.words.models.tags import UserTag, WordTag
from src.apps.common.pagination import PaginatedResult, PaginationParams


class UserTagsRepository(AbstractORMRepository[UserTag]):
    def get_all(self, pagination: PaginationParams, **filters) -> PaginatedResult[UserTag]:
        qs = UserTag.objects.all()
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
    
    def get_by_id(self, obj_id: int) -> Optional[UserTag]:
        return UserTag.objects.get(id=obj_id)
    
    def create(self, **kwargs) -> UserTag:
        return UserTag.objects.create(**kwargs)
    
    def update(self, obj_id: int, **kwargs) -> Optional[UserTag]:
        user_tag = UserTag.objects.get(id=obj_id)
        for key, value in kwargs.items():
            setattr(user_tag, key, value)
        user_tag.save()
        return user_tag
    
    def delete(self, obj_id: int) -> bool:
        user_tag = UserTag.objects.get(id=obj_id)
        user_tag.delete()
        return True
    

class WordTagsRepository(AbstractORMRepository[WordTag]):
    def get_all(self, pagination: PaginationParams, **filters) -> PaginatedResult[WordTag]:
        qs = WordTag.objects.all()
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
    
    def get_by_id(self, obj_id: int) -> Optional[WordTag]:
        return WordTag.objects.get(id=obj_id)
    
    def create(self, **kwargs) -> WordTag:
        return WordTag.objects.create(**kwargs)
    
    def update(self, obj_id: int, **kwargs) -> Optional[WordTag]:
        word_tag = WordTag.objects.get(id=obj_id)
        for key, value in kwargs.items():
            setattr(word_tag, key, value)
        word_tag.save()
        return word_tag
    
    def delete(self, obj_id: int) -> bool:
        word_tag = WordTag.objects.get(id=obj_id)
        word_tag.delete()
        return True