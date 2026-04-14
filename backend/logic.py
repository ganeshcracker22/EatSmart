from models import NutritionInfo, FoodTwinSimulation, ConsequenceEngine, Recommendation
from data import FOOD_DATA, ALTERNATIVES

def simulate_twin(nutrition: NutritionInfo, goal: str) -> FoodTwinSimulation:
    # Rule-based simulation
    energy_change = (nutrition.calories / 2000) * 100
    
    fat_risk = "low"
    if nutrition.calories > 300 or nutrition.sugar > 15:
        fat_risk = "high"
    elif nutrition.calories > 200 or nutrition.sugar > 5:
        fat_risk = "medium"
        
    muscle_support = "low"
    if nutrition.protein > 20:
        muscle_support = "high"
    elif nutrition.protein > 10:
        muscle_support = "medium"
        
    sugar_spike = "low"
    if nutrition.sugar > 30:
        sugar_spike = "high"
    elif nutrition.sugar > 10:
        sugar_spike = "medium"
        
    return FoodTwinSimulation(
        energy_change_pct=round(energy_change, 2),
        fat_storage_risk=fat_risk,
        muscle_support=muscle_support,
        sugar_spike=sugar_spike
    )

def calculate_consequences(nutrition: NutritionInfo) -> ConsequenceEngine:
    # Immediate effect
    if nutrition.sugar > 20:
        immediate = f"You'll likely experience a sharp insulin spike within 30 minutes, potentially followed by a 'sugar crash' that leaves you feeling fatigued."
    elif nutrition.calories > 500:
        immediate = f"This is a heavy load for your digestive system. Your body will redirect blood flow to your gut, which might cause some 'brain fog' or lethargy shortly after eating."
    elif nutrition.protein > 20:
        immediate = f"The high protein content will promote immediate satiety, making you feel full and focused for the next few hours."
    else:
        immediate = "Your metabolism will remain relatively stable, providing a consistent but modest energy release without a major insulin response."
        
    # Short term (7 days)
    if nutrition.sugar > 10:
        short = "Over the next week, frequent intake of this profile could increase your cravings for high-carb foods and lead to minor water retention around your midsection."
    elif nutrition.protein > 20:
        short = "If you keep this up for a week, you'll notice improved muscle recovery and a steadier appetite throughout the day."
    else:
        short = "A week of this nutritional balance typically maintains your current baseline without significant changes in body composition or energy levels."
        
    # Long term (90 days)
    if nutrition.fats > 20 or nutrition.sugar > 15:
        long = "Persistent consumption over 3 months significantly increases the risk of visceral fat storage and could begin to impact your metabolic flexibility and insulin sensitivity."
    elif nutrition.protein > 25:
        long = "90 days of this pattern, combined with training, would likely result in measurable lean muscle gains and a more efficient resting metabolic rate."
    else:
        long = "Long-term, this profile supports general maintenance, though it may lack the specific surplus or deficit needed for aggressive body transformation goals."
        
    return ConsequenceEngine(
        immediate_effect=immediate,
        short_term_effect=short,
        long_term_risk=long
    )

def calculate_risk_score(nutrition: NutritionInfo) -> int:
    # Formula: (Calories/10 + Sugar*5 + Fat*2) - (Protein*3)
    score = (nutrition.calories / 10 + nutrition.sugar * 5 + nutrition.fats * 2) - (nutrition.protein * 3)
    return max(0, min(100, int(score)))

def get_recommendation(food_name: str, nutrition: NutritionInfo, current_score: int) -> Recommendation:
    food_key = food_name.lower()
    category = "healthy carbs" # default
    
    if food_key in FOOD_DATA:
        category = FOOD_DATA[food_key]["category"]
    
    alt_name = ALTERNATIVES.get(category, "Grilled Chicken")
    
    # Simple risk reduction logic
    reduction = 0.0
    if current_score > 30:
        reduction = 40.0
    elif current_score > 60:
        reduction = 75.0
        
    return Recommendation(
        suggested_alternative=alt_name,
        risk_reduction_pct=reduction
    )
