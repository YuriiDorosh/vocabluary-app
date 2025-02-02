from typing import Optional
from django.contrib.auth.models import User
from django.db.models import QuerySet
from src.apps.common.repositories import AbstractORMRepository
from src.api.v1.ninja.filters import PaginationIn


class UserRepository(AbstractORMRepository[User]):

    def get_all(
        self,
        pagination: PaginationIn,
        ) -> QuerySet[User]:
        return User.objects.all()[pagination.offset:pagination.offset + pagination.limit]
    
    def get_user_count(self) -> int:
        return User.objects.all().count()

    def get_by_id(self, obj_id: int) -> Optional[User]:
        try:
            return User.objects.get(id=obj_id)
        except User.DoesNotExist:
            return None

    def create(self, **kwargs) -> User:
        user = User(**kwargs)
        user.set_password(kwargs.get("password"))
        user.save()
        return user

    def update(self, obj_id: int, **kwargs) -> Optional[User]:
        user = self.get_by_id(obj_id)
        if user:
            for field, value in kwargs.items():
                setattr(user, field, value)
            user.save()
        return user

    def delete(self, obj_id: int) -> bool:
        user = self.get_by_id(obj_id)
        if user:
            user.delete()
            return True
        return False
