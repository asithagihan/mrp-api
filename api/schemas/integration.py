from pydantic import BaseModel


class IntegrationBase(BaseModel):
    name: str
    url: str


class IntegrationCreate(IntegrationBase):
    api_key: str | None = None
    api_secret: str | None = None
    pass


class Integration(IntegrationBase):
    id: int
    account_id: int

    class Config:
        from_attributes = True
