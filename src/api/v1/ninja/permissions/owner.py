from ninja_extra import permissions
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request: HttpRequest, controller, obj: User) -> bool:
        return obj.author == request.user