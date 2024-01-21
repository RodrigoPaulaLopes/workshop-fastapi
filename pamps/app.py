from fastapi import FastAPI

app = FastAPI(title="Pamps", version='0.1.0', description="Pamps is a post app")


@app.get("/")
async def hello():
    return {"hello": "world aaaaa"}

