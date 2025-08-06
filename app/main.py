import os
from fastapi import FastAPI
from fastapi_blocks import BlockManager

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BLOCKS_FOLDER = "projects" # Could be wtv

app = FastAPI()
block_manager = BlockManager(blocks_folder=os.path.join(CURRENT_DIR, BLOCKS_FOLDER))
app = block_manager.init_app(app)