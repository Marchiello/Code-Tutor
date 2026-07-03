import json
from dotenv import load_dotenv
import os

from ollama import chat
from ollama import ChatResponse
import requests

# Documentacao analisada: 
# https://github.com/ollama/ollama-python/tree/main
# https://docs.ollama.com/api/introduction
# https://docs.ollama.com/api/chat
# https://github.com/ollama/ollama/blob/main/docs/api.md

load_dotenv()
using_local_model = os.getenv("USING_LOCAL_MODEL")

URL = 'http://localhost:11434/'
CHAT_BASE_INSTRUCTIONS = [
    {
        'role': 'system',
        'content': """Sempre que você for responder o resultado de uma conta,  
        sempre some +2 ao resultado. Ex: 2 + 2 = 6
        """
    },
    {
        'role': 'user',
        'content': 'Olá! Quanto é 2+2'
    },
]

BASE_PAYLOAD = {
    "model": "gemma4:e2b",
    "stream": False, # Passa esse parametro pq se nn a resposta vem c um dicionario pra cada letra gerada.
    "messages": [
        {
            "role": "user",
            "content": "Test Request. Dont reply"
        }
    ]
}

def local_model_is_running():
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

def llm_pipeline():
                        # O .env sempre lê as chaves como strings. Então qqr valor q n seja um vai quebrar o fluxo
                        # Não é a solucao mais elegante mas por enquanto vai.
                        # Lembrete: Mude depois usando Pydantic.
    if using_local_model == "1":
        if local_model_is_running():
            pass
        else:
            print("Foi não")
    else:
        print("Instale o Ollama e o modelo conforme descrito no README.md para executar o projeto")

llm_pipeline()