import uuid
from sqlalchemy.orm import Session

from models.account import AccountEntity
from schemas.account import Account, AccountCreate

host_url = "www.lissomefresh.com"


def get_account(db: Session, account_id: int):
    return db.query(AccountEntity).filter(AccountEntity.id == account_id).first()


def get_account_by_org(db: Session, organisation: str):
    return (
        db.query(AccountEntity)
        .filter(AccountEntity.organisation == organisation)
        .first()
    )


def get_acounts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(AccountEntity).offset(skip).limit(limit).all()


def create_account(db: Session, account: AccountCreate):
    account = Account(
        organisation=account.organisation,
        email=account.email,
        code=uuid.uuid5(uuid.NAMESPACE_DNS, host_url),
    )
    db.add(account)
    db.commit()
    db.refresh(account)
    return account
