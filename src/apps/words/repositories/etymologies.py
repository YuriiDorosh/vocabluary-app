from django.db.models import QuerySet
from typing import Optional
from src.apps.common.repositories import AbstractORMRepository
from src.apps.words.models.etymologies import WordEtymology
from src.apps.common.pagination import PaginatedResult, PaginationParams


class EtymologiesRepository(AbstractORMRepository[WordEtymology]):
    def get_all(self, pagination: PaginationParams, **filters) -> PaginatedResult[WordEtymology]:
        qs = WordEtymology.objects.all()
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
    
    def get_by_id(self, obj_id: int) -> Optional[WordEtymology]:
        return WordEtymology.objects.get(id=obj_id)
    
    def create(self, **kwargs) -> WordEtymology:
        return WordEtymology.objects.create(**kwargs)
    
    def update(self, obj_id: int, **kwargs) -> Optional[WordEtymology]:
        word_etymology = WordEtymology.objects.get(id=obj_id)
        for key, value in kwargs.items():
            setattr(word_etymology, key, value)
        word_etymology.save()
        return word_etymology
    
    def delete(self, obj_id: int) -> bool:
        word_etymology = WordEtymology.objects.get(id=obj_id)
        word_etymology.delete()
        return True