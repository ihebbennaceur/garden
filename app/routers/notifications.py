from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.notification import Recommendation
from app.schemas.notification import Recommendation, RecommendationCreate
from app.core.security import get_current_user
from app.models.user import User

router = APIRouter()

@router.get("/", response_model=list[Recommendation])
def get_user_recommendations(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return db.query(Recommendation).filter(Recommendation.user_id == current_user.id).all()