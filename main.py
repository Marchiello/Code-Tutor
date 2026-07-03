from fastapi import FastAPI

# Documentacao Analisada:
# https://fastapi.tiangolo.com/reference/fastapi/#fastapi.FastAPI
# https://fastapi.tiangolo.com/tutorial/first-steps/

app = FastAPI(
    title="API do Code-Tutor"
)

@app.get("/", status_code=200)
async def root():
    return {"status": "Active"}