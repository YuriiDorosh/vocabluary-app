from django.db.models import QuerySet
from typing import Optional
from src.apps.common.repositories import AbstractORMRepository
from src.apps.words.models.antonyms import WordAntonym
from src.apps.common.pagination import PaginatedResult, PaginationParams


class AntonymsRepository(AbstractORMRepository[WordAntonym]):
    def get_all(self, pagination: PaginationParams, **filters) -> PaginatedResult[WordAntonym]:
        qs = WordAntonym.objects.all()
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
    
    def get_by_id(self, obj_id: int) -> Optional[WordAntonym]:
        return WordAntonym.objects.get(id=obj_id)
    
    def create(self, **kwargs) -> WordAntonym:
        return WordAntonym.objects.create(**kwargs)
    
    def update(self, obj_id: int, **kwargs) -> Optional[WordAntonym]:
        word_antonym = WordAntonym.objects.get(id=obj_id)
        for key, value in kwargs.items():
            setattr(word_antonym, key, value)
        word_antonym.save()
        return word_antonym
    
    def delete(self, obj_id: int) -> bool:
        word_antonym = WordAntonym.objects.get(id=obj_id)
        word_antonym.delete()
        return True