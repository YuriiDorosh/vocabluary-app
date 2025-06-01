from django.db.models import QuerySet
from typing import Optional
from src.apps.common.repositories import AbstractORMRepository
from src.apps.words.models.synonyms import WordSynonym
from src.apps.common.pagination import PaginatedResult, PaginationParams


class SynonymsRepository(AbstractORMRepository[WordSynonym]):
    def get_all(self, pagination: PaginationParams, **filters) -> PaginatedResult[WordSynonym]:
        qs = WordSynonym.objects.all()
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
    
    def get_by_id(self, obj_id: int) -> Optional[WordSynonym]:
        return WordSynonym.objects.get(id=obj_id)
    
    def create(self, **kwargs) -> WordSynonym:
        return WordSynonym.objects.create(**kwargs)
    
    def update(self, obj_id: int, **kwargs) -> Optional[WordSynonym]:
        word_synonym = WordSynonym.objects.get(id=obj_id)
        for key, value in kwargs.items():
            setattr(word_synonym, key, value)
        word_synonym.save()
        return word_synonym
    
    def delete(self, obj_id: int) -> bool:
        word_synonym = WordSynonym.objects.get(id=obj_id)
        word_synonym.delete()
        return True