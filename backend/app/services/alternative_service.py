from typing import List, Dict

class AlternativeService:
    """Service to suggest Tunisian alternatives"""
    
    tunisian_products = {
        "beverages": [
            {"name": "Hamoud Boualem", "type": "Soda", "origin": "Algeria/Tunisia"},
            {"name": "Boga", "type": "Soda", "origin": "Tunisia"},
            {"name": "Safia", "type": "Water", "origin": "Tunisia"},
            {"name": "Ain Garci", "type": "Water", "origin": "Tunisia"},
        ],
        "dairy": [
            {"name": "Vitalait", "type": "Milk & Yogurt", "origin": "Tunisia"},
            {"name": "Delice", "type": "Dairy products", "origin": "Tunisia"},
            {"name": "Soummam", "type": "Dairy products", "origin": "Algeria"},
        ],
        "snacks": [
            {"name": "Tounsi", "type": "Chips", "origin": "Tunisia"},
            {"name": "Crazy", "type": "Snacks", "origin": "Tunisia"},
            {"name": "Bimo", "type": "Biscuits", "origin": "Tunisia"},
        ],
        "cleaning": [
            {"name": "Crystal", "type": "Detergent", "origin": "Tunisia"},
            {"name": "Isis", "type": "Soap", "origin": "Tunisia"},
        ],
        "coffee": [
            {"name": "Tunisian coffee shops", "type": "Coffee", "origin": "Tunisia"},
            {"name": "Local cafes", "type": "Coffee", "origin": "Tunisia"},
        ],
        "restaurants": [
            {"name": "Tunisian restaurants", "type": "Fast food", "origin": "Tunisia"},
            {"name": "Local eateries", "type": "Food", "origin": "Tunisia"},
        ],
    }
    
    @staticmethod
    def get_alternatives(category: str) -> List:
        """Get alternatives by category"""
        return AlternativeService.tunisian_products.get(category.lower(), [])
    
    @staticmethod
    def get_categories() -> List[str]:
        """Get all available categories"""
        return list(AlternativeService.tunisian_products.keys())
    
    @staticmethod
    def search_alternatives(query: str) -> List:
        """Search for alternatives across all categories"""
        results = []
        query_lower = query.lower()
        
        for category, products in AlternativeService.tunisian_products.items():
            for product in products:
                if query_lower in product["name"].lower():
                    results.append({**product, "category": category})
        
        return results