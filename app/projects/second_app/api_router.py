from fastapi import APIRouter, Request

router = APIRouter(prefix='/app')

@router.get("/")
async def read_root(request: Request):
    return { "message" : "received" }