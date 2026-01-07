from typing import Dict, Optional
from app.core.config import settings

class AIProductMatcher:
    """AI-powered product matching and analysis"""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or settings.ANTHROPIC_API_KEY
        if self.api_key:
            try:
                from anthropic import Anthropic
                self.client = Anthropic(api_key=self.api_key)
            except ImportError:
                self.client = None
        else:
            self.client = None
    
    def match_product(self, product_name: str) -> Dict:
        """Match product using AI"""
        if not self.client:
            return {
                "error": "AI service not configured",
                "fallback": True
            }
        
        prompt = f"""Analyze this product: {product_name}

Determine:
1. Is it on a boycott list? (Yes/No)
2. What category does it belong to? (beverages, dairy, snacks, etc.)
3. Suggest 3 Tunisian alternatives

Return ONLY valid JSON with this structure:
{{
    "is_boycotted": true/false,
    "category": "category_name",
    "alternatives": ["alt1", "alt2", "alt3"]
}}"""
        
        try:
            message = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=1024,
                messages=[{"role": "user", "content": prompt}]
            )
            
            return {
                "success": True,
                "ai_response": message.content[0].text
            }
        except Exception as e:
            return {
                "error": str(e),
                "fallback": True
            }
    
    def analyze_image(self, image_data: bytes) -> Dict:
        """Analyze product image using AI"""
        if not self.client:
            return {"error": "AI service not configured"}
        
        # Placeholder for image analysis
        return {"message": "Image analysis not yet implemented"}