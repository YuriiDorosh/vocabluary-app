from django.db.models import QuerySet
from typing import Optional
from src.apps.common.repositories import AbstractORMRepository
from src.apps.words.models.words import Word
from src.apps.common.pagination import PaginatedResult, PaginationParams


class WordsRepository(AbstractORMRepository[Word]):
    def get_all(self, pagination: PaginationParams, **filters) -> PaginatedResult[Word]:
        qs = Word.objects.all()
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
    
    def get_by_id(self, obj_id: int) -> Optional[Word]:
        return Word.objects.get(id=obj_id)
    
    def create(self, **kwargs) -> Word:
        return Word.objects.create(**kwargs)
    
    def update(self, obj_id: int, **kwargs) -> Optional[Word]:
        word = Word.objects.get(id=obj_id)
        for key, value in kwargs.items():
            setattr(word, key, value)
        word.save()
        return word
    
    def delete(self, obj_id: int) -> bool:
        word = Word.objects.get(id=obj_id)
        word.delete()
        return True