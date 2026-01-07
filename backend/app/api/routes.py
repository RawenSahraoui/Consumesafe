from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from app.services.boycott_service import BoycottService
from app.services.alternative_service import AlternativeService

router = APIRouter()

class ProductCheck(BaseModel):
    product_name: str

@router.post("/check-product")
async def check_product(product: ProductCheck):
    """Check if a product is on the boycott list"""
    try:
        result = BoycottService.check_product(product.product_name)
        
        return {
            "product_name": product.product_name,
            "is_boycotted": result["is_boycotted"],
            "reason": result.get("reason"),
            "alternatives": result.get("alternatives", [])
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/alternatives/{category}")
async def get_alternatives(category: str):
    """Get Tunisian alternatives by category"""
    alternatives = AlternativeService.get_alternatives(category)
    
    if not alternatives:
        raise HTTPException(status_code=404, detail=f"No alternatives found for category: {category}")
    
    return {"category": category, "alternatives": alternatives}

@router.get("/categories")
async def get_categories():
    """Get all available product categories"""
    categories = AlternativeService.get_categories()
    return {"categories": categories}

@router.get("/boycott-list")
async def get_boycott_list():
    """Get the complete boycott list"""
    boycott_list = BoycottService.get_all_boycotted()
    return {"boycott_list": boycott_list}