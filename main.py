from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config_db import Base, engine
from controllers.music_controller import router as music_router

def get_application():
    """Instancia una nueva aplicación de FastAPI pre-configurada"""

    # Creamos la base de datos
    Base.metadata.create_all(bind=engine)

    # Creamos la aplicación de fastAPI
    app = FastAPI(title="Proyecto 2 - Music Store", version="1.0.0", description="Manuel Da Pena")

    # Habilitamos CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Incluimos los Routers
    app.include_router(music_router, prefix="/music-store/api/v1")

    return app

app = get_application()