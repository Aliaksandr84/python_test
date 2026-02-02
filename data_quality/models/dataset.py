from sqlalchemy import Column, Integer, String, DateTime, func
from .base import Base

class Dataset(Base):
    __tablename__ = "dataset"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    path = Column(String, nullable=False)
    uploaded_at = Column(DateTime, default=func.now())