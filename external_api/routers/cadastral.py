import random

# import time
from fastapi import APIRouter
from .schemas import Cadastral

router = APIRouter()


@router.post("/")
async def root(cadastral_data: Cadastral):
    status: bool = bool(random.getrandbits(1))
    # time.sleep(5)
    return {"status": status}
