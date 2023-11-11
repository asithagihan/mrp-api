from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class IntegrationEntity(Base):
    __tablename__ = "integrations"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    name = Column(String, index=True)
    url = Column(String)
    api_key = Column(String)
    api_secret = Column(String)
    account_id = Column(Integer, ForeignKey("accounts.id"))

    account = relationship("Account", back_populates="integrations")
