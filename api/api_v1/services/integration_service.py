from sqlalchemy.orm import Session
from models.integration import IntegrationEntity
from schemas.integration import IntegrationCreate


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
