import os
import openai
import spacy
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_APY_KEY')
openai.api_key = api_key

modelo = "text-davinci-002"
prompt = "Cuenta una historia breve"

respuesta = openai.Completion.create(
        engine=modelo,
        prompt=prompt,
        n=1,     #nos indica la cantidad de respuestas que queremos obtener
        max_tokens=100  #max_tokens le indica el máximo de la respuesta
        
)

texto_generado = respuesta.choices[0].text.strip()
print(texto_generado)

print("***")

modelo_spacy = spacy.load("es_core_news_md")
analisis = modelo_spacy(texto_generado)

for token in analisis:
    print(token.text, token.pos_)  #Este ciclo for muestra cada uno de los tokens que componen el texto, pero añadiendo , token.pos_ nos trae la categoria gramatical de cada token
