from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from item_bill_of_materials import item_bill_of_materials_table
from database import Base


class BillOfMaterials(Base):
    __tablename__ = "bill_of_materials"

    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey("items.id"))
    quantity = Column(Integer)
    operation = Column(Integer, default=1)
    description = Column(String(255))

    items = relationship(
        "Item",
        secondary=item_bill_of_materials_table,
        back_populates="bill_of_materials",
    )

    def __repr__(self):
        return f"<BillOfMaterials {self.id} {self.quantity}>"
