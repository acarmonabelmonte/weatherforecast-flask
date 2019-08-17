import requests
import argparse
import sys

parser = argparse.ArgumentParser()

# Inputs para el script
parser.add_argument('--city', help='Ciudad a obtener el tiempo')
args = parser.parse_args()
city = args.city

# Realizamos la petición GET si la ciudad se encuentra entre las opciones de ejemplo
# API-endpoint
api_endpoint = "http://127.0.0.1:5000/weather-forecast/"

# URL
url = api_endpoint + city

# Realizar solicitud GET sobre la url pasada
r = (requests.get(url)).json()

# Aplicamos la fórmula 'C = K - 273.15' en Temperature para obtener ésta en grados Celsius, ya que la API de Openweathermap
# nos facilita este dato en grados Kelvin.  
result = 'Weather forecast for tomorrow in ' + city.capitalize() + ' Temperature: ' + str(round(r['main']['temp'] - 273.15, 2)) + ' ºC'
print(result)