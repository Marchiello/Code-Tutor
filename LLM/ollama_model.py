import json
from dotenv import load_dotenv
import os

from ollama import chat
from ollama import ChatResponse
import requests

load_dotenv()

using_local_model = os.getenv("USING_LOCAL_MODEL")
ollama_model = os.getenv("OLLAMA_MODEL")

# Documentacao analisada: 
# https://github.com/ollama/ollama-python/tree/main
# https://docs.ollama.com/api/introduction
# https://docs.ollama.com/api/chat
# https://github.com/ollama/ollama/blob/main/docs/api.md

URL = 'http://localhost:11434/'

def local_model_is_running():
    """Verifica se o servidor Olamma está disponivel."""
    try:
        # Converte p dicionario com o .json pq se nn tu n consegue acessar as chaves
        # Aqui so to observando o status_code, ent n precisei converter.
        res = requests.get(url=URL)
        if res.status_code == 200:
            return True
        else:
            raise Exception
    except Exception as e:
        print(e)
        return False

def create_exercise(language: str = "Python", exercise_type: str = "Programming Logic"):

    if not local_model_is_running:
        return {"status": "500", "content": "Erro ao criar exercício: O Ollama não está rodando."}

    """Cria um novo exercício com base nos argumentos recebidos."""

    proggraming_language = language
    exercise_t = exercise_type

    CHAT_BASE_INSTRUCTIONS = [
        {
            'role': 'system',
            'content': f"""
            Like a expert programming instructor, design a exercise in {proggraming_language} to a begginer programming student.
            The exercise should involve a pratical, real-world application and be developed within a single code file.

            The problem statement must be in Portuguese-BR. Be direct and provide only the problem statement. Say nothing more than necessary.
            """
        },
    ]

    BASE_PAYLOAD = {
        "model": f"{ollama_model}",
        "stream": False, # Passa esse parametro pq se nn a resposta vem c um dicionario pra cada letra gerada.
        "messages": CHAT_BASE_INSTRUCTIONS
    }

    try:
        
        res = requests.post(url=URL+"api/chat", json=BASE_PAYLOAD).json()
        return(res["message"]["content"])
    except Exception as e:
        print(e)

def llm_pipeline():
                        # O .env sempre lê as chaves como strings. Então qqr valor q n seja um vai quebrar o fluxo
                        # Não é a solucao mais elegante mas por enquanto vai.
                        # Lembrete: Mude depois usando Pydantic.
    if using_local_model == "1":
        if local_model_is_running():
            create_exercise()
        else:
            print("Foi não")
    else:
        print("Instale o Ollama e o modelo conforme descrito no README.md para executar o projeto")

# llm_pipeline()