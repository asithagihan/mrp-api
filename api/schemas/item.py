from pydantic import BaseModel, Field


class ItemCreate(BaseModel):
    group_id: int = Field(..., gt=0)
    group_name: str = Field(...)
    unit: str = Field(...)
    item_type: str = Field(...)
    product_type: str = Field(...)
    description: str = Field(...)
    name: str = Field(...)
    rate: int = Field(..., gt=0)
    purchase_rate: int = Field(..., gt=0)
    reorder_level: int = Field(..., gt=0)
    initial_stock: int = Field(..., gt=0)
    initial_stock_rate: int = Field(..., gt=0)
    vendor_id: int = Field(..., gt=0)
    vendor_name: str = Field(...)
    sku: str = Field(...)
    upc: int = Field(...)
    ean: int = Field(...)
    isbn: int = Field(...)
    part_number: int = Field(...)
    attribute_option_name1: str = Field(...)
    purchase_description: str = Field(...)


class ItemUpdate(BaseModel):
    group_id: int = Field(...)
    group_name: str = Field(...)
    unit: str = Field(...)
    item_type: str = Field(...)
    product_type: str = Field(...)
    description: str = Field(...)
    name: str = Field(...)
    rate: int = Field(...)
    purchase_rate: int = Field(...)
    reorder_level: int = Field(...)
    initial_stock: int = Field(...)
    initial_stock_rate: int = Field(...)
    vendor_id: int = Field(...)
    vendor_name: str = Field(...)
    sku: str = Field(...)
    upc: int = Field(...)
    ean: int = Field(...)
    isbn: int = Field(...)
    part_number: int = Field(...)
    attribute_option_name1: str = Field(...)
    purchase_description: str = Field(...)


class Item(BaseModel):
    id: int
    group_id: int
    group_name: str
    unit: str
    item_type: str
    product_type: str
    description: str
    name: str
    rate: int
    purchase_rate: int
    reorder_level: int
    initial_stock: int
    initial_stock_rate: int
    vendor_id: int
    vendor_name: str
    sku: str
    upc: int
    ean: int
    isbn: int
    part_number: int
    attribute_option_name1: str
    purchase_description: str
