from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class AccountEntity(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    code = Column(String)
    is_active = Column(Boolean, default=True)

    integrations = relationship("Integration", back_populates="account")
