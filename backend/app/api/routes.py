from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from app.services.boycott_service import BoycottService
from app.services.alternative_service import AlternativeService
from app.ml.matcher import AIProductMatcher
from app.core.config import settings
from slowapi import Limiter
from slowapi.util import get_remote_address

router = APIRouter()
limiter = Limiter(key_func=get_remote_address)

# Initialize AI matcher
ai_matcher = AIProductMatcher(settings.ANTHROPIC_API_KEY)

class ProductCheck(BaseModel):
    product_name: str
    use_ai: bool = False

@router.post("/check-product")
@limiter.limit("20/minute")
async def check_product(product: ProductCheck, request: Request):
    """Check if a product is boycotted with optional AI enhancement"""
    try:
        # Basic check
        result = BoycottService.check_product(product.product_name)
        
        # AI enhancement if requested and available
        if product.use_ai and ai_matcher.client:
            ai_result = ai_matcher.match_product(product.product_name)
            result["ai_enhanced"] = True
            result["ai_confidence"] = ai_result.get("confidence", 0)
        
        return {
            "product_name": product.product_name,
            "is_boycotted": result["is_boycotted"],
            "reason": result.get("reason"),
            "alternatives": result.get("alternatives", []),
            "ai_enhanced": result.get("ai_enhanced", False)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/alternatives/{category}")
@limiter.limit("30/minute")
async def get_alternatives(category: str, request: Request):
    """Get Tunisian alternatives by category"""
    alternatives = AlternativeService.get_alternatives(category)
    
    if not alternatives:
        raise HTTPException(status_code=404, detail=f"No alternatives found for category: {category}")
    
    return {"category": category, "alternatives": alternatives}

@router.get("/categories")
@limiter.limit("50/minute")
async def get_categories(request: Request):
    """Get all available product categories"""
    categories = AlternativeService.get_categories()
    return {"categories": categories}

@router.get("/boycott-list")
@limiter.limit("30/minute")
async def get_boycott_list(request: Request):
    """Get the complete boycott list"""
    boycott_list = BoycottService.get_all_boycotted()
    return {"boycott_list": boycott_list, "total": len(boycott_list)}