from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref

from database import Base


class ProductionOrderTemplate(Base):
    __tablename__ = "production_order_templates"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(255))

    job_templates = relationship("JobTemplate", backref="production_order_templates")

    def __repr__(self):
        return f"<ProductionOrderTemplate {self.id} {self.name}>"
