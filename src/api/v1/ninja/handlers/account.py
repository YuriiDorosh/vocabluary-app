from ninja import Query
from ninja.constants import NOT_SET
from ninja_extra import (
    api_controller,
    route,
    permissions,
)
from ninja_jwt.authentication import JWTAuth
from django.contrib.auth.models import User
from django.http import HttpRequest
from src.api.v1.ninja.permissions.owner import IsAccountOwner
from src.api.v1.ninja.base_schemas import ApiResponse, ListPaginatedResponse
from src.api.v1.ninja.filters import PaginationIn, PaginationOut
from src.api.v1.ninja.schemas.account import AccountIn, AccountOut
from src.apps.auth.repositories.auth_repository import UserRepository
from src.api.meta import get_meta_data


@api_controller("/account", auth=NOT_SET, permissions=[permissions.AllowAny])
class AccountController:
    def __init__(self):
        self.user_repository = UserRepository()
        
    @route.get(
        "/{user_id}/",
        response=ApiResponse[AccountOut],
        auth=JWTAuth(),
        permissions=[permissions.IsAuthenticated],
    )
    def get_account_by_user_id(
        self,
        request: HttpRequest,
        user_id: int,
    ) -> ApiResponse[AccountOut]:
        user = self.user_repository.get_by_id(
            obj_id=user_id
        )
        
        data = AccountOut.to_entity(user)
        
        return ApiResponse(
            data=data,
            meta=get_meta_data(request=request),
            errors=[],
        )
        
    @route.get(
        "/list",
        response=ApiResponse[ListPaginatedResponse[AccountOut]],
        auth=JWTAuth(),
        permissions=[permissions.IsAuthenticated],
    )
    def get_all_accounts(
        self,
        request: HttpRequest,
        pagination_in: Query[PaginationIn],
    ) -> ApiResponse[ListPaginatedResponse[AccountOut]]:
        users = self.user_repository.get_all(
            pagination=pagination_in
        )
        users_count = self.user_repository.get_user_count()
        
        items = [AccountOut.to_entity(user) for user in users]
        
        pagination_out = PaginationOut(
            offset=pagination_in.offset,
            limit=pagination_in.limit,
            total=users_count,
        )
        
        return ApiResponse(
            data=ListPaginatedResponse(items=items, pagination=pagination_out),
            meta=get_meta_data(request=request),
            errors=[],
        )

    @route.post(
        "/", 
        response=ApiResponse[AccountOut],
        auth=NOT_SET,
        permissions=[permissions.AllowAny],
    )
    def create_account(
        self,
        request: HttpRequest,
        create_account_data: AccountIn
    ) -> ApiResponse[AccountOut]:
        user = self.user_repository.create(
            username=create_account_data.username,
            password=create_account_data.password,
            email=create_account_data.email,
        )
        
        data =  AccountOut.to_entity(user)

        return ApiResponse[AccountOut](
            data=data,
            meta=get_meta_data(request),
            errors=[],
        )