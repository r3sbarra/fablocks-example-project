from sqlmodel import SQLModel, create_engine
from fastapi_blocks import BlockManager
from importlib import import_module

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)

def create_db():
    block_manager = BlockManager()
    
    modules_to_import = block_manager.get_schemas()
    
    for module_name in modules_to_import:
        try:
            module = import_module(module_name)
        except:
            print(f"Failed to import module: '{module_name}'")
            
    SQLModel.metadata.create_all(engine)