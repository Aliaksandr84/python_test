from sqlalchemy import Column, Integer, String, ForeignKey
from .base import Base

class ColumnCheck(Base):
    __tablename__ = "column_check"
    id = Column(Integer, primary_key=True)
    report_id = Column(Integer, ForeignKey('quality_report.id'))
    column_name = Column(String, nullable=False)
    null_count = Column(Integer, nullable=False)