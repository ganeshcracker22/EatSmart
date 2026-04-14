from pydantic import BaseModel
from typing import Optional, List

class FoodAnalysisRequest(BaseModel):
    food_name: Optional[str] = None
    image: Optional[str] = None
    user_goal: str  # "weight loss" or "muscle gain"

class NutritionInfo(BaseModel):
    calories: int
    protein: float
    carbs: float
    fats: float
    sugar: float

class FoodTwinSimulation(BaseModel):
    energy_change_pct: float
    fat_storage_risk: str  # low/medium/high
    muscle_support: str    # low/medium/high
    sugar_spike: str       # low/medium/high

class ConsequenceEngine(BaseModel):
    immediate_effect: str
    short_term_effect: str
    long_term_risk: str

class Recommendation(BaseModel):
    suggested_alternative: str
    risk_reduction_pct: float

class FoodAnalysisResponse(BaseModel):
    food_name: str
    nutrition: NutritionInfo
    simulation: FoodTwinSimulation
    consequences: ConsequenceEngine
    risk_score: int
    recommendation: Recommendation
