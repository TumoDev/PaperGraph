import requests, re
from bs4 import BeautifulSoup
from Levenshtein import distance
from googlesearch import search as search_google


def find_paper_arxiv(paper_name):
    best_match_score = float('inf')
    best_match_pdf_url = None
    max_results = 10

    query = paper_name.replace(" ", "+")

    search_url = "https://arxiv.org/search/"
    params = {
        "query": query,
        "searchtype": "all",
        "source": "header"
    }

    with requests.Session() as session:
        response = session.get(search_url, params=params)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")

        summary_url_elements = soup.find_all("a", href=re.compile("https://arxiv.org/abs/"), limit=max_results)

        for elem in summary_url_elements:
            response = session.get(elem.get("href"))
            response.raise_for_status()

            soup = BeautifulSoup(response.content, "html.parser")

            title_element = soup.find("h1", class_="title mathjax")
            if title_element and title_element.span:
                title_element.span.extract()
                paper_title = title_element.text.strip()

                #titles distance
                score = distance(paper_name, paper_title)

                if score < best_match_score:
                    best_match_score = score
                    pdf_button_element = soup.find("a", class_="abs-button download-pdf")

                    if pdf_button_element:
                        best_match_pdf_url = "https://arxiv.org" + pdf_button_element.get("href")

    return best_match_pdf_url

def find_doi(name):
    """Encuentra el DOI de un paper basado en su nombre."""
    excluded = "https://arxiv.org"
    result = set()
    for idx, url in enumerate(search_google(name, num=10)):
        if idx >= 5:
            break
        if excluded not in url:
            result.add(url)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0"
    }
    doi_pattern = re.compile(r'https://doi.org/[a-zA-Z0-9/.]+', re.IGNORECASE)
    doi_results = set()
    
    for url in result:
        try:
            with requests.Session() as session:
                response = session.get(url, headers=headers)
                response.raise_for_status()
                soup = BeautifulSoup(response.content, "html.parser")
                dois = re.findall(doi_pattern, soup.prettify())
                doi_results.update(dois)
        except requests.RequestException:
            # Este bloque se ejecutará si hay algún error al hacer la solicitud.
            # Puedes optar por imprimir un mensaje o simplemente continuar.
            #print(f"Error accessing URL: {url}")
            continue  # Continuar con el siguiente URL en el loop

    return list(doi_results)

"""Links Sci-Hub"""
def create_scihub_link(dois):
    """Crea enlaces directos para Sci-Hub usando una lista de DOIs."""
    base_url = "https://sci-hub.se/"
    links = []

    if dois:#si esta vacia no entra
        for doi in dois:
            # Extraer solo el segmento DOI
            doi_segment = doi.split("https://doi.org/")[1]
            scihub_url = base_url + doi_segment
            links.append(scihub_url)
    return links
