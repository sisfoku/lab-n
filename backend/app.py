from fastapi import FastAPI
from pydantic import BaseModel
from ai.prompt import generate_food_recommendation

app = FastAPI(
    title="NutriAI API",
    description="AI Food Recommendation System"
)


class FoodRequest(BaseModel):
    preference: str



@app.get("/")
def home():

    return {
        "project": "NutriAI",
        "message": "AI Food Recommendation API Running"
    }



@app.post("/recommend")
def recommend_food(data: FoodRequest):

    prompt = generate_food_recommendation(
        data.preference
    )


    return {

        "input": data.preference,

        "ai_prompt": prompt,

        "recommendation": {

            "food": "Salad Ayam Panggang",

            "nutrition": [
                "Protein tinggi",
                "Serat",
                "Vitamin"
            ],

            "benefit": [
                "Mendukung kesehatan tubuh",
                "Membantu pola makan sehat"
            ]

        }

    }