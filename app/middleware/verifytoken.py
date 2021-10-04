from typing import Optional
import os
from fastapi import Header, HTTPException

async def verify_token(x_access_token: str = Header(...)):
    if x_access_token != os.getenv('ACCESS_TOKEN'):
        raise HTTPException(
            status_code=400, detail="x-access-token header invalid")
