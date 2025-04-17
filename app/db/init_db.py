from app.db.database import SessionLocal
from app.models.user import User

def init_db():
    db = SessionLocal()
    
    # Créer un admin si nécessaire
    admin = db.query(User).filter(User.email == "admin@example.com").first()
    if not admin:
        admin_user = User(
            email="admin@example.com",
            name="Admin",
            hashed_password=get_password_hash("adminpassword"),
            is_admin=True
        )
        db.add(admin_user)
        db.commit()
        db.refresh(admin_user)
        print("Admin user created")
    
    db.close()