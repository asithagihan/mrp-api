from sqlalchemy import Column, Integer, Float, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref

from database import Base


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True)
    production_order_id = Column(Integer, ForeignKey("production_orders.id"))
    status = Column(String(255))
    production_order = relationship("ProductionOrder", back_populates="jobs")

    bill_of_materials = relationship("JobBillOfMaterials", back_populates="jobs")

    def __repr__(self):
        return f"<Job {self.id} {self.status}>"
