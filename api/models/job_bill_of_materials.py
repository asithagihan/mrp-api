from sqlalchemy import Column, Integer, Float, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref

from database import Base


class JobBillOfMaterials(Base):
    __tablename__ = "job_bill_of_materials"

    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey("items.id"))
    quantity = Column(Integer)

    items = relationship("Item", back_populates="bill_of_materials")

    def __repr__(self):
        return f"<JobBillOfMaterials {self.id} {self.quantity}>"
