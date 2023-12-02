from sqlalchemy import Column, Integer, ForeignKey, Table

from database import Base


class BillOfMaterialItem(Base):
    __tablename__ = "bill_of_materials_items"

    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    operation = Column(Integer, default=1)
    bill_of_material_id = Column(Integer, ForeignKey("bill_of_material.id"))

    def __repr__(self):
        return f"<BillOfMaterialItem {self.id}>"
