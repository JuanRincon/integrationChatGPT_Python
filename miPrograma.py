import os
import openai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_APY_KEY')
openai.api_key = api_key

modelo = "text-davinci-002"
prompt = "Elige un buen nombre para un elefante"

respuesta = openai.Completion.create(
        engine=modelo,
        prompt=prompt,
        n=1,     #nos indica la cantidad de respuestas que queremos obtener
        temperature=0.1,    #temperature es el nivel creatividad que se quiere siendo 0.1 el menor y 1 mayor
        max_tokens=100  #max_tokens le indica el máximo de la respuesta
        
)

for idx, opcion in enumerate(respuesta.choices):
    texto_generado = opcion.text.strip()
    print(f"Respuesta {idx + 1}: {texto_generado}\n")
