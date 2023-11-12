from sqlalchemy import Column, Integer, ForeignKey, Table

from database import Base

item_bill_of_materials_table = Table(
    "item_bill_of_materials",
    Base.metadata,
    Column("item_id", Integer, ForeignKey("item.id")),
    Column("bill_of_materials_id", Integer, ForeignKey("bill_of_materials.id")),
)
