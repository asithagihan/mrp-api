from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref

from database import Base


class ProductionOrder(Base):
    __tablename__ = "production_orders"

    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    status = Column(String(255))

    def __repr__(self):
        return f"<ProductionOrder {self.id} {self.quantity}>"
