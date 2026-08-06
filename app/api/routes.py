from fastapi import APIRouter
from app.api.v1.health import router as health_router
from app.api.v1.products import router as products_router

api_router = APIRouter()
api_router.include_router(health_router, prefix="/health", tags=["Health"])
api_router.include_router(products_router, prefix="/api/v1/products", tags=["Products"])
