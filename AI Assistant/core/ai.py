import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("COLE AQUI A API")

client = genai.Client(api_key=api_key)


def responder_ia(msg, contexto=None):
    if contexto is None:
        contexto = []

    prompt = f"""
Você é um assistente financeiro especialista.

Histórico:
{contexto}

Usuário: {msg}

Responda de forma clara, profissional e educativa.
"""

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return response.text