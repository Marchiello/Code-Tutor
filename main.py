from fastapi import FastAPI

from src.llm.ollama_model import create_exercise
from src.database import postgresql

# Documentacao Analisada:
# https://fastapi.tiangolo.com/reference/fastapi/#fastapi.FastAPI
# https://fastapi.tiangolo.com/tutorial/first-steps/

app = FastAPI(
    title="API do Code-Tutor"
)

@app.get("/", status_code=200)
async def root():
    return {"status": "Active"}

@app.get("/new_exercise")
async def new_exercise(language: str = "Python", exercise_type: str = "Programming Logic"):
    create_exercise(language, exercise_type)

@app.post("/save_exercise")
async def save_exercise(statement, resolution):
    await postgresql.save_exercise(statement=statement, solution=resolution)

@app.get("/get_exercises")
async def get_exercises():
    await postgresql.get_exercises()