from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI(
    title="NutriAI API",
    version="1.0.0",
    description="AI Food Recommendation System"
)


# CORS supaya frontend bisa akses API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# ==========================
# REQUEST MODEL
# ==========================

class FoodRequest(BaseModel):
    age: int
    gender: str
    weight: float
    height: float
    goal: str
    diet: str
    preference: str



# ==========================
# HOME
# ==========================

@app.get("/")
def home():

    return {
        "project": "NutriAI",
        "message": "AI Food Recommendation API Running"
    }



# ==========================
# AI RECOMMENDATION
# ==========================

@app.post("/recommend")
def recommend_food(data: FoodRequest):

    preference = data.preference.lower()
    goal = data.goal.lower()
    diet = data.diet.lower()



    # LOW CALORIE / DIET
    if (
        "low" in preference
        or "calorie" in preference
        or "weight" in goal
        or "diet" in goal
    ):

        result = {

            "food": "Grilled Chicken Salad",

            "nutrition": [
                "Protein tinggi",
                "Kalori rendah",
                "Serat",
                "Vitamin"
            ],

            "benefit": [
                "Membantu menurunkan berat badan",
                "Membuat kenyang lebih lama",
                "Menjaga pola makan sehat"
            ]
        }



    # VEGETARIAN

    elif (
        "vegetarian" in diet
        or "vegan" in diet
    ):

        result = {

            "food": "Buddha Bowl Sayuran",

            "nutrition": [
                "Protein nabati",
                "Serat tinggi",
                "Vitamin",
                "Mineral"
            ],

            "benefit": [
                "Baik untuk kesehatan pencernaan",
                "Mendukung pola makan seimbang",
                "Membantu memenuhi nutrisi harian"
            ]
        }



    # HIGH PROTEIN

    elif (
        "protein" in preference
        or "muscle" in goal
        or "fitness" in goal
    ):

        result = {

            "food": "Chicken Rice Bowl",

            "nutrition": [
                "Protein tinggi",
                "Karbohidrat",
                "Vitamin B",
                "Mineral"
            ],

            "benefit": [
                "Membantu pembentukan otot",
                "Mendukung pemulihan tubuh",
                "Menambah energi"
            ]
        }



    # LOW CARB

    elif "carb" in preference:

        result = {

            "food": "Salmon dengan Sayuran",

            "nutrition": [
                "Protein",
                "Omega 3",
                "Serat",
                "Mineral"
            ],

            "benefit": [
                "Membantu menjaga gula darah",
                "Baik untuk metabolisme",
                "Menjaga kesehatan jantung"
            ]
        }



    # DEFAULT

    else:

        result = {

            "food": "Salad Ayam Panggang",

            "nutrition": [
                "Protein tinggi",
                "Serat",
                "Vitamin",
                "Mineral"
            ],

            "benefit": [
                "Mendukung kesehatan tubuh",
                "Membantu pola makan sehat",
                "Menjaga energi harian"
            ]
        }



    return {

        "input": data.preference,

        "user": {

            "age": data.age,
            "gender": data.gender,
            "weight": data.weight,
            "height": data.height,
            "goal": data.goal,
            "diet": data.diet

        },

        "recommendation": result

    }