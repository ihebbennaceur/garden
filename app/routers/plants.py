from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.plant import Plant, UserPlant, PlantRequest
from app.schemas.plant import Plant, UserPlant, UserPlantCreate, PlantRequest, PlantRequestCreate
from app.core.security import get_current_user
from app.models.user import User

router = APIRouter()

@router.get("/", response_model=list[Plant])
def get_all_plants(db: Session = Depends(get_db)):
    return db.query(Plant).all()

@router.get("/my-plants", response_model=list[UserPlant])
def get_user_plants(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return db.query(UserPlant).filter(UserPlant.user_id == current_user.id).all()

@router.post("/my-plants", response_model=UserPlant)
def add_user_plant(
    plant: UserPlantCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_plant = db.query(Plant).filter(Plant.id == plant.plant_id).first()
    if not db_plant:
        raise HTTPException(status_code=404, detail="Plant not found")
    
    db_user_plant = UserPlant(
        user_id=current_user.id,
        plant_id=plant.plant_id,
        nickname=plant.nickname
    )
    db.add(db_user_plant)
    db.commit()
    db.refresh(db_user_plant)
    return db_user_plant

@router.post("/requests", response_model=PlantRequest)
def submit_plant_request(
    request: PlantRequestCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_request = PlantRequest(
        user_id=current_user.id,
        name=request.name,
        description=request.description,
        image_url=request.image_url
    )
    db.add(db_request)
    db.commit()
    db.refresh(db_request)
    return db_request