import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from models import FoodAnalysisRequest, FoodAnalysisResponse, NutritionInfo
from data import FOOD_DATA
from logic import simulate_twin, calculate_consequences, calculate_risk_score, get_recommendation

# Load environment variables
load_dotenv()

app = FastAPI(title="EatSmart AI Backend")

# Configuration for Stitch API (can be used in future integrations)
STITCH_API_KEY = os.getenv("STITCH_API_KEY")
STITCH_SERVER_URL = os.getenv("STITCH_SERVER_URL")

# Enable CORS for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static assets
# Ensure the 'assets' directory exists before mounting
if os.path.exists("assets"):
    app.mount("/assets", StaticFiles(directory="assets"), name="assets")

# Serve the futuristic frontend at the root
@app.get("/")
def read_index():
    if os.path.exists("index.html"):
        return FileResponse("index.html")
    return {"message": "NutriTwin Backend is active. Frontend index.html not found."}

@app.get("/app.js")
def read_app_js():
    if os.path.exists("app.js"):
        return FileResponse("app.js")
    return HTTPException(status_code=404, detail="app.js not found")

@app.get("/")
def read_root():
    return {"message": "NutriTwin Risk AI Backend is running."}

@app.post("/analyze-food", response_model=FoodAnalysisResponse)
def analyze_food(request: FoodAnalysisRequest):
    # Determine food name
    food_name = request.food_name
    
    # If image is provided and food_name is not, try to 'detect' it
    # For this hackathon version, we check if the image string contains a known food name
    if not food_name and request.image:
        image_str = request.image.lower()
        for known_food in FOOD_DATA.keys():
            if known_food in image_str:
                food_name = known_food
                break
    
    if not food_name:
        raise HTTPException(status_code=400, detail="Could not identify food from food_name or image.")
    
    food_key = food_name.lower()
    
    # Nutritional logic
    # If food is not in our mock DB, we return a fallback or error
    if food_key in FOOD_DATA:
        food_stats = FOOD_DATA[food_key]
    else:
        # Fallback to a generic profile for unknown foods to stay 'hackathon-ready'
        food_stats = {
            "calories": 200,
            "protein": 5.0,
            "carbs": 25.0,
            "fats": 8.0,
            "sugar": 5.0,
            "category": "unknown"
        }
    
    nutrition = NutritionInfo(
        calories=food_stats["calories"],
        protein=food_stats["protein"],
        carbs=food_stats["carbs"],
        fats=food_stats["fats"],
        sugar=food_stats["sugar"]
    )
    
    # Logic Engine
    simulation = simulate_twin(nutrition, request.user_goal)
    consequences = calculate_consequences(nutrition)
    risk_score = calculate_risk_score(nutrition)
    recommendation = get_recommendation(food_name, nutrition, risk_score)
    
    return FoodAnalysisResponse(
        food_name=food_name,
        nutrition=nutrition,
        simulation=simulation,
        consequences=consequences,
        risk_score=risk_score,
        recommendation=recommendation
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
