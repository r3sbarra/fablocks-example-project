from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi_blocks import BlockManager

block_manager = BlockManager()
router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return block_manager.templates.TemplateResponse("index.html", context={"request": request})