# Imports
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
# to execute run -> uvicorn name_file:app --reload

@app.get("/")
async def root():
    return {"message" : "Root configurado basico"}


class Resp(BaseModel):
    valor_1 : int
    valor_2 : int
    operacao : str


@app.post("/api")
async def api(valor1: int, valor2: int, valor3: str):
    if valor3 == "soma":
        soma = valor1+valor2
    
    elif valor3 == "subtração":
        soma = valor1-valor2
    
    elif valor3 == "divisão":
        soma = valor1/valor2
    
    elif valor3 == "multiplicação":
        soma = valor1*valor2

    return f"A soma dos resultados é = {soma}"