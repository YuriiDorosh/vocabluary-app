from ninja_extra import permissions, api_controller, http_post
from django.http import HttpRequest


@api_controller("/resset_password", permissions=[permissions.AllowAny])
class RessetPasswordController:
    @http_post("/")
    def resset_password(self, request: HttpRequest, title: str):
        return {"message": f"Post '{title}' created by {request.user.username}"}