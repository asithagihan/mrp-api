from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from schemas.account import Account
from auth import cognito
from schemas.integration import Integration, IntegrationCreate
from database import get_db
from api_v1.services.integration_service import get_integrations, create_integration
from account import get_account

router = APIRouter()


@router.get("/", response_model=list[Integration])
def get(
    account: Account = Depends(get_account),
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    items = get_integrations(db, account_id=account.id, skip=skip, limit=limit)
    return items


@router.post("/", response_model=Integration)
def create(
    integration: IntegrationCreate,
    account: Account = Depends(get_account),
    db: Session = Depends(get_db),
):
    return create_integration(db=db, integration=integration, account_id=account.id)


@router.post("/zoho/auth", response_model=list[Integration])
def get(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    return []


@router.get("/zoho/jwt", response_model=list[Integration])
def get(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    return []


@router.get("/zoho/callback", response_model=list[Integration])
def get(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    return []
