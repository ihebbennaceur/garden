from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PlantBase(BaseModel):
    name: str
    description: str

class PlantCreate(PlantBase):
    image_url: str
    created_by_admin: bool = True

class Plant(PlantBase):
    id: int
    image_url: str
    created_by_admin: bool

    class Config:
        orm_mode = True

class UserPlantBase(BaseModel):
    plant_id: int
    nickname: Optional[str]

class UserPlantCreate(UserPlantBase):
    pass

class UserPlant(UserPlantBase):
    id: int
    user_id: int
    date_added: datetime

    class Config:
        orm_mode = True

class PlantRequestBase(BaseModel):
    name: str
    description: str
    image_url: str

class PlantRequestCreate(PlantRequestBase):
    pass

class PlantRequest(PlantRequestBase):
    id: int
    user_id: int
    date_submitted: datetime
    is_approved: bool

    class Config:
        orm_mode = True