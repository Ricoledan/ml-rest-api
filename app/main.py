from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()
app = FastAPI()

origins = ["*"]

app.add_middleware(CORSMiddleware, allow_origins=origins)


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
