from app.types.healthcheck import HealthCheck
from typing import Optional
import os
from fastapi import Depends, FastAPI, Header, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from middleware.verifytoken import verify_token
from routes import models

load_dotenv()

app = FastAPI()
origins = ["*"]

app.add_middleware(CORSMiddleware, allow_origins=origins)
app.include_router(models.router)


@app.get('/')
def root():
    return "Machine Learning REST API Service"


@ app.get("/api/logs", dependencies=[Depends(verify_token)])
def read_logs():
    return "TBA"


@ app.post("/api/healthcheck")
def healthcheck(hc: HealthCheck):
    return hc
