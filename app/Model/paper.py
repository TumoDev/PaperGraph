from cgitb import text
from csv import reader
from PyPDF2 import PdfReader
from bs4 import BeautifulSoup
from . import search
import os, requests, re
from . import GPT

class Paper:
    def __init__(self, name: str, author: str, date: str, id_name_location: str):
        self._name=name
        self._author=author
        self._date=date
        self._id_name_location=id_name_location
        self._content=None
        self._location="./assets/papers/"+id_name_location+".pdf"
        self._references=None 

            
    @property
    def name(self):
        return self._name
 
    @property
    def author(self):
        return self._author
    
    @property
    def date(self):
        return self._date
    
    @property
    def id_name_location(self):
        return self._id_name_location
    
    @property
    def location(self):
        return self._location
    
    @property
    def content(self):
        return self._content
    
    @property
    def references(self):
        return self._references

    def set_ubication(self, ubication: str):
        self._ubication=ubication

    def set_location(self, location: str):
        self._location=location

    def set_content(self):
        texto_completo=self.extract_complete_text()
        self._content=GPT.extract_tokens(texto_completo)

    def set_references(self,content):
        self._references=content

    def __str__(self) -> str:
        return f"'{self._name}' por '{self._author}'"
    
    def verify_paper(self,response):
        try:
            # Abre el archivo PDF en modo de lectura binaria
            with open(self._location, 'rb') as file:
                # Crea un objeto PdfReader para leer el archivo PDF
                reader = PdfReader(file)

                # Verifica si el PDF tiene páginas; retorna False si está vacío
                if len(reader.pages) == 0:
                    return False

                # Extrae el texto de la primera página del PDF
                first_page = reader.pages[0]
                text = first_page.extract_text()

                # Si hay texto extraído de la página
                if text:
                    # Busca la palabra "Abstract" y recorta el texto hasta esa posición
                    position = text.find("Abstract")
                    text = text[:position] if position != -1 else text

                    # Compara el nombre del paper (en minúsculas) con el texto (también en minúsculas)
                    if self._name.lower() in text.lower():
                        return True  # Retorna True si el nombre está en el texto
                # Retorna False si el nombre del paper no se encuentra en el texto
                return False

        except Exception as e:
            # Imprime un mensaje de error si ocurre una excepción y retorna False
            print(f"Error al leer el PDF: {e}")
            return False
    
    def download_web_pdf(self, url: str): #usada en arxiv
        response = requests.get(url)
        if response.status_code == 200:
                with open(self._location, "wb") as archivo:
                    archivo.write(response.content)
                return True
        return False

    def encontrar_paper(url: str): 
        try:
            # Obtener el contenido de la página
            response = requests.get(url)
            response.raise_for_status()  # Lanzar excepción si hay algún problema

            # Parsear el contenido con BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Buscar el div con class "content"
            content_div = soup.find('div', class_='content')

            # Si no se encuentra la clase 'content', retornamos True
            if not content_div:
                return True

            # Buscar el id "smile" dentro de content_div
            smile_id = content_div.find(id='smile')

            # Si se encuentra el id "smile", retornamos False, de lo contrario retornamos True
            return smile_id is None
        except requests.RequestException:
            print("Hubo un problema al acceder a la URL.")
            return False  # Puedes decidir qué hacer en caso de excepción
    
    def descargar_pdf(url: str): #desde sciHub
        try:
            # Realiza una petición a la página web
            response = requests.get(url)
            response.raise_for_status()

            # Analiza el contenido de la página con BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Encuentra todos los botones con el id "buttons"
            buttons = soup.find_all(id="buttons")

            for btn in buttons:
                # Extrae la URL de descarga del atributo onclick
                download_url = btn.button['onclick'].split("'")[1]

                # Si la URL comienza con "//", añade "https:" al principio
                if download_url.startswith("//"):
                    download_url = "https:" + download_url

                # Descarga el archivo
                filename = download_url.split("/")[-1].split("?")[0]
                with requests.get(download_url, stream=True) as r:
                    r.raise_for_status()
                    with open(filename, "wb") as f:
                        for chunk in r.iter_content(chunk_size=8192):
                            f.write(chunk)

            # Si todo salió bien, retorna True
            return filename

        except Exception as e:
            # En caso de error, imprime el error y retorna False
            print(f"Error al descargar: {e}")
            return False
    
    def download_paper(self):
        # Buscar en ArXiv
        url = search.find_paper_arxiv(self.name)
        if url:
            if self.download_web_pdf(url):
                return True

        # Buscar DOIs
        doi_results = search.find_doi(self.name)
        if doi_results:
            sci_links = search.create_scihub_link(doi_results)  # Genera links Sci-Hub
            for link in sci_links:
                if self.encontrar_paper(link):
                    downloaded_file = self.descargar_pdf(link)  # Obtén el nombre del archivo descargado
                    if downloaded_file:  # Si se descargó el archivo correctamente
                        ruta = "/content/" + downloaded_file
                        if self.verify_paper(self.name, ruta):
                            return True  # Si coincide, finaliza con éxito
                        else:
                            os.remove(ruta)  # Elimina el archivo si no pasa la verificación
            return False

        # Retorna False si no se encuentra el paper ni en ArXiv ni a través de DOIs
        return False
    
    def extract_complete_text(self):
        with open(self.location, 'rb') as archivo:
            reader=PdfReader(archivo)
            
            # Extraer todo el texto del PDF
            texto_completo = ""
            for page in reader.pages:
                texto_completo += page.extract_text() + "\n"
            
            if not texto_completo:
                return False
            return texto_completo
    

    def extract_references(self):
        #extract all text
        texto_completo=self.extract_complete_text()
        
        # Encontrar la última ocurrencia de la palabra "Referencia"
        indice_referencia = texto_completo.rfind("Referencia")

        # Extraer texto desde la última palabra "Referencia" hasta el final
        if indice_referencia != -1:
            text_references = texto_completo[indice_referencia:]
        else:
            text_references = ""

        self.set_references(text_references)

        if self.references:
            return True
        return False
    
    