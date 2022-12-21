from config_db import SessionLocal

def get_db():
    """Función helper para obtener una session de la base de datos"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()