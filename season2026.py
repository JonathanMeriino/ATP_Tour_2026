import requests
from bs4 import BeautifulSoup
import pandas as pd

# 1. Configurar la URL y los encabezados para evitar bloqueos
url = "https://www.atptour.com/es/news/what-is-the-2026-atp-tour-calendar"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

try:
    # 2. Obtener el contenido de la página
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8' # Asegurar que los caracteres en español se lean bien
    soup = BeautifulSoup(response.text, 'html.parser')

    # 3. Buscar la tabla de datos
    # En esta página específica, la tabla está dentro del cuerpo del artículo
    tabla_html = soup.find('table')

    if tabla_html:
        # 4. Leer la tabla con pandas
        # Convertimos el objeto de BeautifulSoup a string para que pandas lo procese
        df = pd.read_html(str(tabla_html))[0]

        # 5. Guardar el archivo CSV
        # Usamos encoding='utf-8-sig' para que Excel reconozca los caracteres especiales
        nombre_archivo = "calendario_atp_2026.csv"
        df.to_csv(nombre_archivo, index=False, encoding='utf-8-sig', sep=';')
        
        print(f"✅ ¡Éxito! El archivo '{nombre_archivo}' ha sido generado.")
        print("Aquí tienes una vista previa de los datos:")
        print(df.head())
    else:
        print("❌ No se encontró ninguna tabla en la página.")

except Exception as e:
    print(f"❌ Ocurrió un error: {e}")