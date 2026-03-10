import os
from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel('gemini-1.5-flash')

app = FastAPI(title="Chatbot IA API")

class MensagemUsuario(BaseModel):
    texto: str

@app.get("/")
def read_root():
    return {"status": "ok", "mensagem": "Backend do Chatbot rodando com sucesso!"}

@app.post("/chat")
def conversar_com_ia(mensagem: MensagemUsuario):
    resposta_ia = model.generate_content(mensagem.texto)
    
    return {"resposta": resposta_ia.text}