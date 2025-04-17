from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from app.db.database import Base

class Plant(Base):
    __tablename__ = "plants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    image_url = Column(String)
    created_by_admin = Column(Boolean, default=True)

    user_plants = relationship("UserPlant", back_populates="plant")

class UserPlant(Base):
    __tablename__ = "user_plants"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    plant_id = Column(Integer, ForeignKey("plants.id"))
    nickname = Column(String, nullable=True)
    date_added = Column(DateTime, default=datetime.utcnow)

    owner = relationship("User", back_populates="plants")
    plant = relationship("Plant", back_populates="user_plants")

class PlantRequest(Base):
    __tablename__ = "plant_requests"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String)
    description = Column(String)
    image_url = Column(String)
    date_submitted = Column(DateTime, default=datetime.utcnow)
    is_approved = Column(Boolean, default=False)

    submitter = relationship("User", back_populates="plant_requests")