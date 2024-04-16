"""
Main entrypoint into fastapi app
"""
from fastapi import FastAPI
from routes import api_router

app = FastAPI()


@app.get("/")
def home():
    return {"msg": "Hello Schools"}


app.include_router(api_router)
