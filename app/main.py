from typing import Optional
from functools import wraps
import os
from fastapi import Depends, FastAPI, Header, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

app = FastAPI()
origins = ["*"]

app.add_middleware(CORSMiddleware, allow_origins=origins)


class HealthCheck(BaseModel):
    status: str


async def verify_token(x_access_token: str = Header(...)):
    if x_access_token != os.getenv('ACCESS_TOKEN'):
        raise HTTPException(
            status_code=400, detail="x-access-token header invalid")


@app.get('/')
def root():
    return "Machine Learning REST API Service"


@app.get('/api/model', dependencies=[Depends(verify_token)])
def root(request: Request):
    headers = request.headers
    auth = headers.get('x-access-token')
    print(auth)
    return auth


@ app.get("/api/logs", dependencies=[Depends(verify_token)])
def read_logs():
    return "TBA"


@ app.post("/api/healthcheck")
def healthcheck(hc: HealthCheck):
    return hc
