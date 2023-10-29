
import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_APY_KEY")
openai.api_key = api_key

def crear_contenido(tema, tokens, temperatura, modelo="text-davinci-002"):
    prompt = f"Por favor escribe un artículo corto sobre el tema: {tema}\n\n"
    respuesta = openai.Completion.create(
        engine=modelo,
        prompt=prompt,
        n=1,
        max_tokens=tokens,
        temperature=temperatura
    )
    return respuesta.choices[0].text.strip()

def resumir_text(texto, tokens, temperatura, modelo="text-davici-002"):
    prompt = f"Por favor resume el siguiente texto: {texto}\n\n"
    respuesta = openai.Completion.create(
        engine=modelo,
        prompt=prompt,
        n=1,
        max_tokens=tokens,
        temperature=temperatura
    )
    return respuesta.choices[0].text.strip()

original = input("Pega aquí el artículo que quieres resumir")
tokens = int(input("Cuántos tokens máximos tendrá tu resumen: "))
temperatura = int(input("Del 1 al 10, qué tan creativo quieres que sea tu artículo?: "))/10
resumen = resumir_texto(original, tokens, temperatura)
print(resumen)
