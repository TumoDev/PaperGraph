from pyexpat.errors import messages
from dotenv import load_dotenv
from PyPDF2 import PdfReader
import openai, tiktoken, os, json


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

"""
def extract_tokens(texto, model_gpt="gpt-3.5-turbo"):
    encoding=tiktoken.encoding_for_model(model_gpt)

    # Obtener las primeras 1000 tokens
    texto = texto.split()
    print(texto)
    num_words=0
    num_tokens=0
    for words in texto:
      tokens=len(encoding.encode(text=words))
      num_tokens+=tokens
      if num_tokens>=max_tokens:
        break
      num_words+=1

    return ' '.join(texto[:num_words])
"""

import tiktoken

def extract_tokens(texto, model_gpt="gpt-3.5-turbo", max_tokens=2500):
    # Inicializar el codificador para un modelo específico, como GPT-4
    enc = tiktoken.encoding_for_model(model_gpt)

    # Tokenizar el texto
    tokens = enc.encode(texto)

    # Verificar si el número de tokens solicitado es mayor que la longitud total de tokens
    n_tokens = min(max_tokens, len(tokens))

    # Reconstruir el texto hasta la cantidad especificada de tokens
    text = ''.join([enc.decode([token]) for token in tokens[:n_tokens]])

    return text

def extract_contributions(text_pdf_main, text_references, model_gpt="gpt-3.5-turbo-1106"):

  response = openai.ChatCompletion.create(
     model=model_gpt,
     response_format={ "type": "json_object" },
     messages=[
      {"role": "system", "content": "Eres un asistente designado a responder en JSON."},    
      {"role": "user", "content": "Dame el listado de referencias que salen en el siguiente texto'"+ text_pdf_main +"' a continuacion las referencias'"+ text_references +"'"},
      {"role": "user", "content": "Incluye solo el titulo, nombre, y cantidad de citas dentro del texto"}

      ]
  )
  print(response.choices[0].message.content)
  data = json.loads(response.choices[0].message.content)
  lista_referencias = []
  for referencia in data['referencias']:
      lista_referencias.append(referencia['titulo'])
      lista_referencias.append(referencia['nombre'])
      lista_referencias.append(referencia['citas'])  
  return lista_referencias

#prompt exp regualar 

"""
Necesito ayuda para crear una expresión regular que identifique las referencias bibliográficas en un texto. Las referencias tienen un formato específico donde cada una comienza con un número seguido de un punto, luego el nombre del autor o autores, seguido del título del artículo, el nombre de la publicación o conferencia, detalles de la publicación como el volumen y las páginas, y finalmente el año de publicación. Aquí tienes un ejemplo del texto con las referencias:

"1. Araya, I., Neveu, B., Trombettoni, G.: Exploiting common subexpressions in numerical CSPs. In: Principles and Practice of Constraint Programming (CP 2008), pp. 342–357. Springer (2008). 2. Smith, J., Johnson, M.: Advanced algorithms in computational biology. In: Journal of Computational Biology, vol. 15, no. 3, pp. 457–467. Elsevier (2010)."

Por favor, proporciona una expresión regular que pueda usar para identificar y extraer estas referencias de un texto más extenso para crear objetos `Paper` en Python. Cada objeto `Paper` debe contener el nombre del artículo, los autores, y el año de publicación como atributos.
"""