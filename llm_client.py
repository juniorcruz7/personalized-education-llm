#Gerencia a comunicação com a API do modelo de linguagem e retorna as respostas geradas.
#Gerencia a comunicação com a API do Gemini.

from google import genai
from config import API_KEY, MODEL_NAME

client = genai.Client(api_key=API_KEY)

def call_llm(prompt: str) -> str:
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )
        return response.text

    except Exception as e:
        return f"Erro ao chamar modelo: {e}"
