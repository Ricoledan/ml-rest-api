from typing import Optional
from fastapi import FastAPI
import uvicorn
from dotenv import load_dotenv
from pydantic import BaseModel

# from app.routers import healthcheck

load_dotenv()
app = FastAPI()


class HealthCheck(BaseModel):
    status: str


@app.get('/')
def root():
    return "Machine Learning REST API Service"


@app.post("/api/healthcheck")
def healthcheck(hc: HealthCheck):
    return hc


if __name__ == "__main__":
    uvicorn.run("fastapi_code:app")
