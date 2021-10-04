from fastapi import APIRouter, Depends, Request
from middleware.verifytoken import verify_token

router = APIRouter()


@router.get('/api/model', dependencies=[Depends(verify_token)])
def root(request: Request):
    return 'test model response'
