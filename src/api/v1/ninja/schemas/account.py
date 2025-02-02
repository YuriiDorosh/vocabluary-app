from ninja import Schema
from typing import Optional

class AccountIn(Schema):
    username: str
    email: str
    password: str
    
class AccountOut(Schema):
    id: int
    username: str
    
    @staticmethod
    def to_entity(obj) -> Optional["AccountOut"]:
        if not obj:
            return None
        return AccountOut(
            id=obj.id,
            username=obj.username,
        )