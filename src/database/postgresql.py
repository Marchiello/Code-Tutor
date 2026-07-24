"""Classe responsável por configurar e fazer operações relacionadas ao banco de dados Postgresql."""

from src.common import custom_exceptions

import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

# Documentação Analisada:
# https://pypi.org/project/psycopg2/
#   https://www.psycopg.org/docs/install.html
#   https://github.com/psycopg/psycopg2

# ---------- Atribuição das variáveis de ambiente do BD

db_name = os.getenv("DATABASE_NAME") 
db_user = os.getenv("DATABASE_USER")
db_password = os.getenv("DATABASE_PASSWORD")

# ----------

database = psycopg2.connect(
    f"""
    host=localhost
    dbname={db_name}
    user={db_user}
    password={db_password}
    """
)

cursor = database.cursor()
# records = cursor.fetchall()

# ----------

def database_is_running():
    pass

async def get_exercises():
    
    try:
        exercises = cursor.execute("SELECT * FROM exercises")
        if exercises is None:
            return exercises
    
        else:
            return {"status_code": 204, "message": "Nenhum resultado foi retornado."}
        
    except custom_exceptions.DatabaseException as e:
        print(e)

async def save_exercise(statement, solution, ):
    try:
        exercises = cursor.execute("SELECT * FROM exercises")
        if exercises:
            return exercises
    
        else:
            return {"status_code": 204, "message": "Nenhum resultado foi retornado."}
        
    except custom_exceptions.DatabaseException as e:
        print(e)