from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi_blocks import BlockManager

router = APIRouter(prefix="/app")
bm = BlockManager()

@router.get("", response_class=HTMLResponse)
async def read_root(request: Request):
    return bm.templates.TemplateResponse("second_page.html", context={"request": request})
