from dotenv import load_dotenv
from PyPDF2 import PdfReader
from openai import OpenAI
import tiktoken
import json
import os

MODEL_GPT="gpt-3.5-turbo-1106"
MAX_TOKENS=1000

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=OPENAI_API_KEY)

def Gpt(path):     
    def analyze_references(source):
        prompt = f"""Analyze the text fragment '{source}' and:
        (1) Summarize the main contributions of the source.
        (2) Provide a detailed analysis of the 10 most relevant citations mentioned in the text. For each relevant citation or group of citations, follow these steps:
        (a) Identify the citation(s) in its original format (in brackets or author-year format).
        (b) Explain how the source is related to this citation. Begin with a sentence like: "Related to <citations>, the source..."
        (c) Classify citations in one of the following categories: Modificates, Enhances, Extends, Inspired by, Alternative Techniques, Other.
            - If the source introduces a modification, enhancement, or extension to an existing technique, the reference can be categorized as an "Modificates", "Enhances" or "Extends".
            - If the source's approach is clearly "inspired" by an existing technique, the reference can be categorized as an "Inspired by".
            - References that offer different methods or solutions to the same problem can be classified as "Alternative Techniques."
        (3) Write a JSON File: Structure the analyzed data into a JSON format. Use 'relevant_citations' as the key for the array containing each 'citation', its 'relation' and 'contribution' to the current work, and the 'classification' category (Modificates, Enhances, Extends, Alternative Techniques).
        """
        response = client.chat.completions.create(
            model=MODEL_GPT,
            response_format={ "type": "json_object" },
            messages=[
                {"role": "system", "content": "You are a helpful assistant designed to output JSON"},
                {"role": "user", "content": prompt}
            ]
        )

        create_response = response.choices[0].message.content

        try:
            references_json = json.loads(create_response)
            return json.dumps(references_json, indent=4, ensure_ascii=False)
        except json.JSONDecodeError:
            return "Error: The response is not in valid JSON format."

    def extract_fragment_with_tokens(path):
        encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
        # Leer el PDF y extraer el texto
        with open(path, 'rb') as archivo_entrada:
            lector_pdf = PdfReader(archivo_entrada)
            texto = ""
            for i in range(len(lector_pdf.pages)):
                texto += lector_pdf.pages[i].extract_text() if lector_pdf.pages[i].extract_text() else ""

        # Obtener las primeras MAX_TOKENS tokens
        palabras = texto.split()
        num_tokens = 0
        num_words = 0
        for word in palabras:
            tokens = len(encoding.encode(text=word))
            if num_tokens + tokens > MAX_TOKENS:
                break
            num_tokens += tokens
            num_words += 1

        return ' '.join(palabras[:num_words])
        
    #esta funcion crea lista con indices de referencias
    def list_index_references(json_response):
        try:
            # Parsea el JSON
            data = json.loads(json_response)

            extracted_references = []

            # Procesa las citas
            citations = data.get("relevant_citations", [])
            for citation in citations:
                # Extrae la cita
                citation_text = citation.get("citation", "")
                # Extrae y limpia los índices de las referencias numéricas
                numeric_refs = [ref.strip() for ref in citation_text.strip("[]").split(",") if ref.strip()]
                extracted_references.extend(numeric_refs)

            return extracted_references
        except json.JSONDecodeError:
            return "Error: La respuesta no está en un formato JSON válido."
        
    #Esta funcion almacena toda la parte de referencias dentro del pdf
    def text_references_pdf(path):
        with open(path, 'rb') as file:
            reader = PdfReader(file)
            references_section = ""
            start_extracting = False

            for page in reader.pages:
                text = page.extract_text()

                if 'References' in text:
                    start_extracting = True
                    text = text.split('References')[1] 

                if start_extracting:
                    references_section += text

            return references_section
        
    # Recibe el fragmento de References y los indices de la lista para poder extraer la informacion de cada referencia, almacenandolos en un diccionario
    def info_references(text, reference_numbers):
        extracted_references = {}
        for ref_number in reference_numbers:
            try:
                start_pattern = f"{ref_number}."
                end_pattern = f"{int(ref_number) + 1}."

                start_index = text.find(start_pattern)
                if start_index != -1:
                    end_index = text.find(end_pattern, start_index)

                    if end_index == -1:
                        end_index = len(text)

                    extracted_reference = text[start_index:end_index].strip()
                    extracted_references[ref_number] = extracted_reference
            except Exception as e:
                extracted_references[ref_number] = f"Error processing reference: {e}"

        return extracted_references

    #Este prompt identifica los datos titulo, autor, año para las referencias que tiene el diccionario
    def reference_details(dict):
        prompt = f"""Given a list of academic paper references, extract and structure the details into a consistent JSON format with the following keys for each reference:
        - index (the reference index or ID)
        - author (the author or authors of the work)
        - title (the title of the work)
        - year (the publication year)

        Here are the references:
        {dict}

        Format the details as a JSON object with keys 'index', 'author', 'title', and 'year' for each reference.
    """
        response = client.chat.completions.create(
            model=MODEL_GPT,
            response_format={ "type": "json_object" },
            messages=[
                {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
                {"role": "user", "content": prompt}
            ]
        )

        create_response = response.choices[0].message.content

        try:
            references_json = json.loads(create_response)
            return json.dumps(references_json, indent=4, ensure_ascii=False)
        except json.JSONDecodeError:
            return "Error: The response is not in valid JSON format."
        
    intro_fragment = extract_fragment_with_tokens(path)  # Introduction fragment
    contributions_info = analyze_references(intro_fragment)  # Contributions and references analysis
    indices_array = list_index_references(contributions_info)  # Index references
    text_references_fragment = text_references_pdf(path)  # PDF text fragment
    references_info_dict = info_references(text_references_fragment, indices_array)
    detailed_references = reference_details(references_info_dict)
    references_dict = json.loads(detailed_references)

    return references_dict 