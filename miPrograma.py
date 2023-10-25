import os
import openai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_APY_KEY')
openai.api_key = api_key

modelo = "text-davinci-002"
prompt = "Inventa un poema de 10 palabras sobre python"

respuesta = openai.Completion.create(
        engine=modelo,
        prompt=prompt,
        n=1,     #nos indica la cantidad de respuestas que queremos optener
        temperature=0.1    #temperature es el nivel creatividad que se quiere siendo 0.1 el menor y 1 mayor
)

texto_generado = respuesta.choices[0].text.strip()
print(texto_generado)
