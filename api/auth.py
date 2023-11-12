import os
from typing import Optional
from pydantic_settings import BaseSettings
from pydantic.types import Any
from fastapi_cognito import CognitoAuth, CognitoSettings
from fastapi_cognito import CognitoToken
from pydantic import Field

APP_CLIENT_ID_1 = os.environ["APP_CLIENT_ID_1"]
USERPOOL_ID = os.environ["USERPOOL_ID"]
USERPOOL_REGION = os.environ["USERPOOL_REGION"]


class CustomTokenModel(CognitoToken):
    email: str = Field(alias="email")
    organisation: str = Field(alias="custom:organisation")


class Settings(BaseSettings):
    check_expiration: bool = True
    jwt_header_prefix: str = "Bearer"
    jwt_header_name: str = "Authorization"
    userpools: dict[str, dict[str, Any]] = {
        "eu": {
            "region": USERPOOL_REGION,
            "userpool_id": USERPOOL_ID,
            "app_client_id": [APP_CLIENT_ID_1],  # Example with multiple ids
        }
    }


settings = Settings()
cognito = CognitoAuth(
    settings=CognitoSettings.from_global_settings(settings),
    custom_model=CustomTokenModel,
)
