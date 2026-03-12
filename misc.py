from fastapi import APIRouter, Depends, HTTPException, Request
import random
from slowapi import Limiter
from slowapi.util import get_remote_address
from fastapi import Request



limiter = Limiter(key_func=get_remote_address)

router = APIRouter(prefix="/misc", tags=["misc"])

@router.get("/get_randomize", response_model=int)
@limiter.limit("10/minute")
def get_randomize(request: Request):
    return random.randint(1, 1000)
