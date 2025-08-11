import os
from fastapi import FastAPI
from fastapi_blocks import BlockManager
from starlette.exceptions import HTTPException
from app.db import engine, create_db

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BLOCKS_FOLDER = "projects" # Could be wtv

app = FastAPI()

block_manager = BlockManager(blocks_folder=os.path.join(CURRENT_DIR, BLOCKS_FOLDER))
block_manager.set_db_engine(engine)
create_db()

block_manager.init_app(app)

# Put expections here, or whereever.
@app.exception_handler(HTTPException)
async def not_found(request, exc):
    return block_manager.templates.TemplateResponse("exception.html", context={"request": request, "status_code": exc.status_code})
