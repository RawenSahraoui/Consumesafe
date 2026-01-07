from typing import Dict, List

class BoycottService:
    """Service to check if products are on boycott list"""
    
    boycott_list = {
        # Boissons
        "coca cola": {"reason": "Supporting Israeli occupation", "alternatives": ["Hamoud Boualem", "Boga", "Safia"]},
        "coca-cola": {"reason": "Supporting Israeli occupation", "alternatives": ["Hamoud Boualem", "Boga", "Safia"]},
        "coke": {"reason": "Supporting Israeli occupation", "alternatives": ["Hamoud Boualem", "Boga", "Safia"]},
        "pepsi": {"reason": "Supporting Israeli occupation", "alternatives": ["Boga", "Hamoud Boualem"]},
        "sprite": {"reason": "Coca-Cola product", "alternatives": ["Boga Lim", "Hamoud Lemon"]},
        "fanta": {"reason": "Coca-Cola product", "alternatives": ["Boga Orange", "Hamoud Orange"]},
        "schweppes": {"reason": "Coca-Cola product", "alternatives": ["Hamoud Boualem", "Safia"]},
        
        # Fast Food
        "mcdonald": {"reason": "Supporting Israeli occupation", "alternatives": ["Tunisian restaurants", "Local fast food"]},
        "mcdo": {"reason": "Supporting Israeli occupation", "alternatives": ["Tunisian restaurants", "Local fast food"]},
        "burger king": {"reason": "Supporting Israeli occupation", "alternatives": ["Local burger shops"]},
        "kfc": {"reason": "Supporting Israeli occupation", "alternatives": ["Local chicken restaurants"]},
        "pizza hut": {"reason": "Supporting Israeli occupation", "alternatives": ["Local pizzerias"]},
        "dominos": {"reason": "Supporting Israeli occupation", "alternatives": ["Local pizzerias"]},
        "starbucks": {"reason": "Supporting Israeli occupation", "alternatives": ["Tunisian cafes", "Café culture"]},
        
        # Supermarchés
        "carrefour": {"reason": "Supporting Israeli occupation", "alternatives": ["Magasin General", "Monoprix", "Local markets"]},
        "auchan": {"reason": "Supporting Israeli occupation", "alternatives": ["Geant", "Local markets"]},
        
        # Produits laitiers
        "nestle": {"reason": "Water exploitation", "alternatives": ["Vitalait", "Delice", "Local dairy"]},
        "danone": {"reason": "Economic boycott", "alternatives": ["Vitalait", "Delice"]},
        "activia": {"reason": "Danone product", "alternatives": ["Vitalait yogurt"]},
        "actimel": {"reason": "Danone product", "alternatives": ["Vitalait probiotics"]},
        
        # Hygiène & Beauté
        "loreal": {"reason": "Supporting Israeli occupation", "alternatives": ["Local brands"]},
        "l'oreal": {"reason": "Supporting Israeli occupation", "alternatives": ["Local brands"]},
        "garnier": {"reason": "L'Oreal product", "alternatives": ["Local cosmetics"]},
        "maybelline": {"reason": "L'Oreal product", "alternatives": ["Local makeup"]},
        
        # Technologie
        "hp": {"reason": "Supporting Israeli occupation", "alternatives": ["Dell", "Lenovo", "Local suppliers"]},
        "hewlett packard": {"reason": "Supporting Israeli occupation", "alternatives": ["Dell", "Lenovo"]},
        "siemens": {"reason": "Supporting Israeli occupation", "alternatives": ["Local suppliers"]},
        "soda stream": {"reason": "Israeli company", "alternatives": ["Regular water with lemon"]},
        
        # Snacks
        "pringles": {"reason": "Associated with boycott", "alternatives": ["Tounsi chips", "Crazy"]},
        "lays": {"reason": "PepsiCo product", "alternatives": ["Tounsi chips", "Local snacks"]},
        "doritos": {"reason": "PepsiCo product", "alternatives": ["Local tortilla chips"]},
        
        # Café
        "nescafe": {"reason": "Nestle product", "alternatives": ["Tunisian coffee", "Local brands"]},
        "nespresso": {"reason": "Nestle product", "alternatives": ["Turkish coffee", "Local coffee"]},
        
        # Chocolat
        "kinder": {"reason": "Associated with boycott", "alternatives": ["Local chocolates"]},
        "milka": {"reason": "Associated with boycott", "alternatives": ["Local chocolates"]},
        "toblerone": {"reason": "Associated with boycott", "alternatives": ["Local chocolates"]},
    }
    
    @staticmethod
    def check_product(product_name: str) -> Dict:
        """Check if product is boycotted"""
        product_lower = product_name.lower().strip()
        
        for boycotted_brand, info in BoycottService.boycott_list.items():
            if boycotted_brand in product_lower or product_lower in boycotted_brand:
                return {
                    "is_boycotted": True,
                    "reason": info["reason"],
                    "alternatives": info["alternatives"]
                }
        
        return {
            "is_boycotted": False,
            "reason": None,
            "alternatives": []
        }
    
    @staticmethod
    def get_all_boycotted() -> Dict:
        """Get all boycotted products"""
        return BoycottService.boycott_list
    
    @staticmethod
    def add_boycott(brand: str, reason: str, alternatives: List[str]) -> bool:
        """Add new product to boycott list"""
        brand_lower = brand.lower().strip()
        if brand_lower not in BoycottService.boycott_list:
            BoycottService.boycott_list[brand_lower] = {
                "reason": reason,
                "alternatives": alternatives
            }
            return True
        return False