from fastapi import FastAPI

app = FastAPI(title="Chatbot IA API")

@app.get("/")
def read_root():
    return {"status": "ok", "mensagem": "Backend do Chatbot rodando com sucesso!"}