import os
from sqlalchemy.orm import Session
from models.integration import IntegrationEntity
from schemas.integration import IntegrationCreate

ZOHO_CLIENT_ID = os.environ["ZOHO_CLIENT_ID"]
ZOHO_CLIENT_SECRET = os.environ["ZOHO_CLIENT_SECRET"]
ZOHO_CLIENT_AU = os.environ["ZOHO_CLIENT_AU"]


def get_auth_url():
    URI = "https://accounts.zoho.com.au/"

    ACCESS = "ZohoBooks.fullaccess.all"

    STATE = "testing"

    REDIRECT_URL = "http://localhost:8000/items/zoho/jwt"

    URL = f"{URI}/oauth/v2/auth?scope={ACCESS}&client_id={ZOHO_CLIENT_ID}&state={STATE}&response_type=code&redirect_uri={REDIRECT_URL}&access_type=offline"
    return URL


def get_integrations(db: Session, account_id: int, skip: int = 0, limit: int = 100):
    return (
        db.query(IntegrationEntity)
        .filter(IntegrationEntity.account_id == account_id)
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_integration(db: Session, integration: IntegrationCreate, account_id: int):
    db_item = IntegrationEntity(**integration.model_dump(), account_id=account_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
