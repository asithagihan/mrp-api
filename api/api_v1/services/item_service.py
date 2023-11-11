from sqlalchemy.orm import Session
from models.integration import IntegrationEntity
from schemas.integration import IntegrationCreate


def get_items(db: Session, account_id: int, skip: int = 0, limit: int = 100):
    return (
        db.query(IntegrationEntity)
        .filter(IntegrationEntity.account_id == account_id)
        .offset(skip)
        .limit(limit)
        .all()
    )
