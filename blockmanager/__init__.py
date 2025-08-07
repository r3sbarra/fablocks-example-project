from fastapi import APIRouter

# Import Template Routers
from app.projects.main.router import router as pnpmmlcz
from app.projects.second_app.router import router as ytbsxnru
from app.projects.self_contained.router import router as codtfogu
# === Template Routers End

# Import API Routers
from app.projects.main.api_router import router as ikokfpps
from app.projects.second_app.api_router import router as jymixbzi
# === API Routers End

# Template Router
template_router = APIRouter()

template_router.include_router(pnpmmlcz)
template_router.include_router(ytbsxnru)
template_router.include_router(codtfogu)

# API Router
api_router = APIRouter()

api_router.include_router(ikokfpps)
api_router.include_router(jymixbzi)
