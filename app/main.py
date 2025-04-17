from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, user, plants, notifications
from app.db.database import engine
from app.models import user as user_models, plant as plant_models, notification as notification_models

# Créer les tables de la base de données
user_models.Base.metadata.create_all(bind=engine)
plant_models.Base.metadata.create_all(bind=engine)
notification_models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Plantes App", description="API pour l'application de gestion de plantes", version="1.0.0")

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclure les routeurs
app.include_router(auth.router)
app.include_router(user.router)
app.include_router(plants.router)
app.include_router(notifications.router)

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API Plantes App"}