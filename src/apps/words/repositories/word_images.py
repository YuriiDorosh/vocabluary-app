from django.db.models import QuerySet
from typing import Optional
from src.apps.common.repositories import AbstractORMRepository
from src.apps.words.models.word_images import WordImage
from src.apps.common.pagination import PaginatedResult, PaginationParams


class WordImagesRepository(AbstractORMRepository[WordImage]):
    def get_all(self, pagination: PaginationParams, **filters) -> PaginatedResult[WordImage]:
        qs = WordImage.objects.all()
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
    
    def get_by_id(self, obj_id: int) -> Optional[WordImage]:
        return WordImage.objects.get(id=obj_id)
    
    def create(self, **kwargs) -> WordImage:
        return WordImage.objects.create(**kwargs)
    
    def update(self, obj_id: int, **kwargs) -> Optional[WordImage]:
        word_image = WordImage.objects.get(id=obj_id)
        for key, value in kwargs.items():
            setattr(word_image, key, value)
        word_image.save()
        return word_image
    
    def delete(self, obj_id: int) -> bool:
        word_image = WordImage.objects.get(id=obj_id)
        word_image.delete()
        return True