from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.orm import relationship, backref
from api.models.bill_of_material_item import item_bill_of_materials_table

from database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, nullable=False)
    group_name = Column(String(255), nullable=False)
    unit = Column(String(255), nullable=False)
    item_type = Column(String(255), nullable=False)
    product_type = Column(String(255), nullable=False)
    description = Column(String(255))
    name = Column(String(255), nullable=False)
    rate = Column(Integer, nullable=False)
    purchase_rate = Column(Integer, nullable=False)
    reorder_level = Column(Integer, nullable=False)
    initial_stock = Column(Integer, nullable=False)
    initial_stock_rate = Column(Integer, nullable=False)
    vendor_id = Column(Integer, nullable=False)
    vendor_name = Column(String(255), nullable=False)
    sku = Column(String(255), nullable=False)
    upc = Column(Integer, nullable=False)
    ean = Column(Integer, nullable=False)
    isbn = Column(Integer, nullable=False)
    part_number = Column(Integer, nullable=False)
    attribute_option_name1 = Column(String(255))
    purchase_description = Column(String(255))

    bill_of_material = relationship(
        "BillOfMaterials",
        secondary=item_bill_of_materials_table,
        back_populates="items",
    )

    def __repr__(self):
        return f"<Item {self.id} {self.name}>"
