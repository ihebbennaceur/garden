from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    photo_url = Column(String, nullable=True)
    is_admin = Column(Boolean, default=False)

    plants = relationship("UserPlant", back_populates="owner")
    plant_requests = relationship("PlantRequest", back_populates="submitter")
    recommendations = relationship("Recommendation", back_populates="user")