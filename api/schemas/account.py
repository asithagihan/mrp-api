from pydantic import BaseModel
from schemas.integration import Integration


class AccountBase(BaseModel):
    organisation: str
    email: str


class AccountCreate(AccountBase):
    pass


class Account(AccountBase):
    id: int
    code: str
    is_active: bool
    integrations: list[Integration] = []

    class Config:
        from_attributes = True
