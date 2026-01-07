from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    barcode = Column(String, unique=True, index=True)
    brand = Column(String, index=True)
    is_boycotted = Column(Boolean, default=False)
    reason = Column(String)
    category = Column(String)
    origin_country = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Alternative(Base):
    __tablename__ = "alternatives"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    brand = Column(String)
    origin = Column(String, default="Tunisia")
    category = Column(String, index=True)
    price = Column(Float)
    description = Column(String)
    image_url = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)