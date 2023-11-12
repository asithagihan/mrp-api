from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref

from database import Base


class JobTemplate(Base):
    __tablename__ = "job_templates"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(255))
    bill_of_materials_id = Column(Integer, ForeignKey("bill_of_materials.id"))

    bill_of_materials = relationship("BillOfMaterials", back_populates="job_templates")

    def __repr__(self):
        return f"<JobTemplate {self.id} {self.name}>"
