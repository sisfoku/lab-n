# NutriAI

AI based food recommendation system.


## Features

- AI food recommendation
- REST API
- Nutrition analysis
- Web interface


## Technology

- Python
- FastAPI
- HTML
- AI Prompt Engineering


## Run Backend


Install:

pip install -r backend/requirements.txt


Run:

uvicorn backend.app:app --reload



## API

POST

/recommend


Example:

{
"preference":"makanan rendah kalori"
}
