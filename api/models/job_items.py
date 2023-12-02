from sqlalchemy import Column, Integer, Float, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref

from database import Base


class JobBillOfMaterialsItem(Base):
    __tablename__ = "job_bill_of_materials"

    id = Column(Integer, primary_key=True)
    sku = Column(String(255), nullable=False)
    quantity = Column(Integer)

    def __repr__(self):
        return f"<JobBillOfMaterials {self.id} {self.quantity}>"
