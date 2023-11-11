from pydantic import BaseModel


class DeviceBase(BaseModel):
    name: str
    url: str
