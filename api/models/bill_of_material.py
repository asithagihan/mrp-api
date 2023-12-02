from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from api.models.bill_of_material_item import item_bill_of_materials_table
from database import Base


class BillOfMaterial(Base):
    __tablename__ = "bill_of_materials"

    id = Column(Integer, primary_key=True)
    description = Column(String(255))

    def __repr__(self):
        return f"<BillOfMaterial {self.id} {self.quantity}>"
