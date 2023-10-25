import os
import openai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_APY_KEY')
openai.api_key = api_key

modelos = openai.Model.list()
print(modelos)
