# Importamos las librerías necesarias para hacer el web scraping
import requests  # Para realizar solicitudes HTTP
from bs4 import BeautifulSoup  # Para analizar el contenido HTML

# Definimos la URL de la página que queremos scrapear
url = "http://quotes.toscrape.com/"

# Realizamos una solicitud GET para obtener el contenido de la página
response = requests.get(url)

# Verificamos si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Creamos un objeto BeautifulSoup para analizar el contenido HTML de la página
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Buscamos todas las citas presentes en la página
    citas = soup.find_all("span", class_="text")
    
    # Buscamos todos los autores de las citas en la página
    autores = soup.find_all("small", class_="author")

    # Iteramos sobre las citas y los autores, e imprimimos cada cita con su respectivo autor
    for cita, autor in zip(citas, autores):
        print("Cita:", cita.get_text())  # Imprimimos la cita encontrada
        print("Autor:", autor.get_text())  # Imprimimos el autor de la cita
        print()  # Imprimimos una línea en blanco para separar las citas
else:
    # Si la solicitud no fue exitosa, imprimimos un mensaje de error junto con el código de estado
    print("Error al cargar la página:", response.status_code)
