from django.db.models import QuerySet
from typing import Optional
from src.apps.common.repositories import AbstractORMRepository
from src.apps.words.models.folders import Folder, WordFolder
from src.apps.common.pagination import PaginatedResult, PaginationParams


class FoldersRepository(AbstractORMRepository[Folder]):
    def get_all(self, pagination: PaginationParams, **filters) -> PaginatedResult[Folder]:
        qs = Folder.objects.all()
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
    
    def get_by_id(self, obj_id: int) -> Optional[Folder]:
        return Folder.objects.get(id=obj_id)
    
    def create(self, **kwargs) -> Folder:
        return Folder.objects.create(**kwargs)
    
    def update(self, obj_id: int, **kwargs) -> Optional[Folder]:
        folder = Folder.objects.get(id=obj_id)
        for key, value in kwargs.items():
            setattr(folder, key, value)
        folder.save()
        return folder
    
    def delete(self, obj_id: int) -> bool:
        folder = Folder.objects.get(id=obj_id)
        folder.delete()
        return True
    
    
class WordFoldersRepository(AbstractORMRepository[WordFolder]):
    def get_all(self, pagination: PaginationParams, **filters) -> PaginatedResult[WordFolder]:
        qs = WordFolder.objects.all()
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
    
    def get_by_id(self, obj_id: int) -> Optional[WordFolder]:
        return WordFolder.objects.get(id=obj_id)
    
    def create(self, **kwargs) -> WordFolder:
        return WordFolder.objects.create(**kwargs)
    
    def update(self, obj_id: int, **kwargs) -> Optional[WordFolder]:
        word_folder = WordFolder.objects.get(id=obj_id)
        for key, value in kwargs.items():
            setattr(word_folder, key, value)
        word_folder.save()
        return word_folder
    
    def delete(self, obj_id: int) -> bool:
        word_folder = WordFolder.objects.get(id=obj_id)
        word_folder.delete()
        return True