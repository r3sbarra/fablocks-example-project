from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi_blocks import BlockManager
import os

router = APIRouter(prefix="/app")
templates = BlockManager().templates

@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("second_page.html", context={"request": request})
