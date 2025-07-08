from fastapi import FastAPI
from src.routes.routes import router

app = FastAPI(title="stock trading bot")

app.include_router(router)

@app.get("/")
def home(): 
    return {"message" : "Trading Bot is running"}