from pydantic import BaseModel
from datetime import datetime

class RecommendationBase(BaseModel):
    plant_id: int
    content: str

class RecommendationCreate(RecommendationBase):
    pass

class Recommendation(RecommendationBase):
    id: int
    user_id: int
    date_sent: datetime

    class Config:
        orm_mode = True