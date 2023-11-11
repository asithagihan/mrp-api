from fastapi import HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi_cognito import CognitoToken

from auth import cognito
from database import get_db
from schemas.account import Account


class AccountNotFoundError(HTTPException):
    pass


def get_account(
    auth: CognitoToken = Depends(cognito.auth_required),
    db: Session = Depends(get_db),
) -> Account:
    account = (
        db.query(Account)
        .filter(Account.organisation == auth.organisation)
        .one_or_none()
    )

    if account is None:
        raise AccountNotFoundError()
    return account
