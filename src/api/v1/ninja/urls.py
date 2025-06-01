import asyncio
from time import sleep
from ninja.constants import NOT_SET
from ninja_jwt.controller import NinjaJWTDefaultController
from ninja_extra import NinjaExtraAPI, api_controller, permissions, route
from src.api.v1.ninja.handlers.account import AccountController

api = NinjaExtraAPI()

@api_controller("/ping", auth=NOT_SET, permissions=[permissions.AllowAny])
class PingController:
    @route.get("/test_api_async")
    async def test_api_async(self, request):
        await asyncio.sleep(20)
        return True

    @route.get("/test_api_async_without_sleep")
    async def test_api_async_without_sleep(self, request):
        return True

    @route.get("/test_api_sync")
    def test_api_sync(self, request):
        sleep(20)
        return True

    @route.get("/test_api_sync_without_sleep")
    def test_api_sync_without_sleep(self, request):
        return True

api.register_controllers(NinjaJWTDefaultController)
api.register_controllers(AccountController)
api.register_controllers(PingController)