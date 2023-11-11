from fastapi import APIRouter, HTTPException
from auth import CustomTokenModel
from fastapi import Depends
from sqlalchemy.orm import Session
from auth import cognito
from schemas.account import Account, AccountCreate
from database import get_db
from api_v1.services.account_service import get_account_by_org, create_account

router = APIRouter()


@router.get("/me", response_model=Account)
async def get(
    auth: CustomTokenModel = Depends(cognito.auth_required),
    db: Session = Depends(get_db),
):
    db_account = get_account_by_org(db, organisation=auth.organisation)
    if db_account is None:
        raise HTTPException(status_code=400, detail="Account not found")
    return db_account


@router.post("/", response_model=Account)
def create(
    auth: CustomTokenModel = Depends(cognito.auth_required),
    db: Session = Depends(get_db),
):
    account = AccountCreate(email=auth.email, organisation=auth.organisation)
    db_account = create_account(db, account=account)
    if db_account:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_account(db=db, account=account)
