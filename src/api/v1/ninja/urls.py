from ninja_jwt.controller import NinjaJWTDefaultController
from ninja_extra import NinjaExtraAPI
from src.api.v1.ninja.handlers.account import AccountController

api = NinjaExtraAPI()

api.register_controllers(NinjaJWTDefaultController)
api.register_controllers(AccountController)