from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from schemas.account import Account
from auth import cognito
from schemas.integration import Integration, IntegrationCreate
from database import get_db
from api_v1.services.item_service import get_auth_url

router = APIRouter()


@router.get("/zoho/sync", response_model=list[Integration])
def get(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    return []


@router.get("/", response_model=list[Integration])
def get(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    return []
