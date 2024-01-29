from fastapi import FastAPI
from .routes import main_router
app = FastAPI(title="Pamps", version='0.1.0', description="Pamps is a post app")


@app.get("/")
async def hello():
    return {"message": "Welcome to pamps API v1"}


app.include_router(main_router)