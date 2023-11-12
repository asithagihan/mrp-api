from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref

from database import Base


class ProductionPlan(Base):
    __tablename__ = "production_plans"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(255))

    production_orders = relationship("ProductionOrder", backref="production_plans")

    def __repr__(self):
        return f"<ProductionPlan {self.id} {self.name}>"
