from django.db.models import QuerySet
from typing import Optional
from src.apps.common.repositories import AbstractORMRepository
from src.apps.words.models.translations import WordTranslation
from src.apps.common.pagination import PaginatedResult, PaginationParams


class TranslationsRepository(AbstractORMRepository[WordTranslation]):
    def get_all(self, pagination: PaginationParams, **filters) -> PaginatedResult[WordTranslation]:
        qs = WordTranslation.objects.all()
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
    
    def get_by_id(self, obj_id: int) -> Optional[WordTranslation]:
        return WordTranslation.objects.get(id=obj_id)
    
    def create(self, **kwargs) -> WordTranslation:
        return WordTranslation.objects.create(**kwargs)
    
    def update(self, obj_id: int, **kwargs) -> Optional[WordTranslation]:
        word_translation = WordTranslation.objects.get(id=obj_id)
        for key, value in kwargs.items():
            setattr(word_translation, key, value)
        word_translation.save()
        return word_translation
    
    def delete(self, obj_id: int) -> bool:
        word_translation = WordTranslation.objects.get(id=obj_id)
        word_translation.delete()
        return True