from django.db.models import QuerySet
from typing import Optional
from src.apps.common.repositories import AbstractORMRepository
from src.apps.words.models.examples import WordExample
from src.apps.common.pagination import PaginatedResult, PaginationParams


class ExamplesRepository(AbstractORMRepository[WordExample]):
    def get_all(self, pagination: PaginationParams, **filters) -> PaginatedResult[WordExample]:
        qs = WordExample.objects.all()
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
    
    def get_by_id(self, obj_id: int) -> Optional[WordExample]:
        return WordExample.objects.get(id=obj_id)
    
    def create(self, **kwargs) -> WordExample:
        return WordExample.objects.create(**kwargs)
    
    def update(self, obj_id: int, **kwargs) -> Optional[WordExample]:
        word_example = WordExample.objects.get(id=obj_id)
        for key, value in kwargs.items():
            setattr(word_example, key, value)
        word_example.save()
        return word_example
    
    def delete(self, obj_id: int) -> bool:
        word_example = WordExample.objects.get(id=obj_id)
        word_example.delete()
        return True