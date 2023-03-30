
from fastapi import FastAPI
from .routers.asset import area
from . import models
from .databasecon import engine

from fastapi.middleware.cors import CORSMiddleware

#Not needed due to Alembic
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(area.router)


@app.get("/")
async def root():
    return {"message": "Data Stream API"}