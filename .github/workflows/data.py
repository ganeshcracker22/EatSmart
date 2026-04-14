# Mock Knowledge Base for NutriTwin Risk AI

FOOD_DATA = {
    "burger": {
        "calories": 520,
        "protein": 25.0,
        "carbs": 45.0,
        "fats": 26.0,
        "sugar": 9.0,
        "category": "fast food"
    },
    "pizza": {
        "calories": 570,
        "protein": 24.0,
        "carbs": 68.0,
        "fats": 22.0,
        "sugar": 7.0,
        "category": "fast food"
    },
    "grilled chicken": {
        "calories": 165,
        "protein": 31.0,
        "carbs": 0.0,
        "fats": 3.6,
        "sugar": 0.0,
        "category": "healthy proteins"
    },
    "salad": {
        "calories": 220,
        "protein": 8.0,
        "carbs": 12.0,
        "fats": 16.0,
        "sugar": 4.0,
        "category": "vegetables"
    },
    "soda": {
        "calories": 140,
        "protein": 0.0,
        "carbs": 39.0,
        "fats": 0.0,
        "sugar": 39.0,
        "category": "drinks"
    },
    "apple": {
        "calories": 95,
        "protein": 0.5,
        "carbs": 25.0,
        "fats": 0.3,
        "sugar": 19.0,
        "category": "fruits"
    },
    "oatmeal": {
        "calories": 150,
        "protein": 5.0,
        "carbs": 27.0,
        "fats": 2.5,
        "sugar": 1.0,
        "category": "healthy carbs"
    },
    "protein shake": {
        "calories": 120,
        "protein": 25.0,
        "carbs": 3.0,
        "fats": 1.5,
        "sugar": 1.0,
        "category": "supplements"
    }
}

# Healthy alternatives mapping
ALTERNATIVES = {
    "fast food": "grilled chicken",
    "drinks": "water or green tea",
    "fruits": "apple",
    "healthy proteins": "lentils or boiled eggs",
    "vegetables": "steamed broccoli",
    "healthy carbs": "quinoa",
    "supplements": "greek yogurt"
}
