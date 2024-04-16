"""
Main entrypoint into fastapi app
"""
from fastapi import FastAPI
from routes import api_router
from database import engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"msg": "Hello Schools"}


app.include_router(api_router)
