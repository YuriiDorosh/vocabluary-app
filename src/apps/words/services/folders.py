from typing import Optional
from django.db.models import QuerySet
from src.apps.common.services import BaseService
from src.apps.words.repositories.folders import FoldersRepository, WordFoldersRepository
from src.apps.words.models.folders import Folder, WordFolder
from src.apps.common.pagination import PaginatedResult, PaginationParams


class FoldersService(BaseService[Folder]):
    def __init__(self) -> None:
        repository = FoldersRepository()
        super().__init__(repository)

    def get_all(self, pagination: PaginationParams, **filters) -> PaginatedResult[Folder]:
        return self.repository.get_all(pagination, **filters)

    def get_by_id(self, obj_id: int) -> Optional[Folder]:
        return self.repository.get_by_id(obj_id)

    def create(self, **kwargs) -> Folder:
        return self.repository.create(**kwargs)

    def update(self, obj_id: int, **kwargs) -> Optional[Folder]:
        return self.repository.update(obj_id, **kwargs)

    def delete(self, obj_id: int) -> bool:
        return self.repository.delete(obj_id)
    
    
class WordFoldersService(BaseService[WordFolder]):
    def __init__(self) -> None:
        repository = WordFoldersRepository()
        super().__init__(repository)

    def get_all(self, pagination: PaginationParams, **filters) -> PaginatedResult[WordFolder]:
        return self.repository.get_all(pagination, **filters)

    def get_by_id(self, obj_id: int) -> Optional[WordFolder]:
        return self.repository.get_by_id(obj_id)

    def create(self, **kwargs) -> WordFolder:
        return self.repository.create(**kwargs)

    def update(self, obj_id: int, **kwargs) -> Optional[WordFolder]:
        return self.repository.update(obj_id, **kwargs)

    def delete(self, obj_id: int) -> bool:
        return self.repository.delete(obj_id)