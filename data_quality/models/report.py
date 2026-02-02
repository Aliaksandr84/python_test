from sqlalchemy import Column, Integer, ForeignKey, DateTime, func
from .base import Base

class QualityReport(Base):
    __tablename__ = "quality_report"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    dataset_id = Column(Integer, ForeignKey('dataset.id'))
    checked_at = Column(DateTime, default=func.now())