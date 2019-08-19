import config
import requests
import argparse

parser = argparse.ArgumentParser()

# Ciudades de ejemplo
cities = ['Madrid', 'Barcelona', 'Valencia', 'Sevilla', 'Murcia']

# Inputs para el script
parser.add_argument('--city', help='Ciudad a obtener el tiempo. Por favor, seleccione entre las siguientes opciones: ' +
', '.join(cities))

args = parser.parse_args()

# Realizamos la petición GET si la ciudad se encuentra entre las opciones de ejemplo
city = args.city
if city.capitalize() in cities:
    # API-endpoint
    api_endpoint = "http://" + str(config.host) + ":" + str(config.port)

    # URL
    url = api_endpoint + "/" + city

    # Realizar solicitud GET sobre la url pasada
    r = (requests.get(url)).json()

    # Aplicamos la fórmula 'C = K - 273.15' en Temperature para obtener ésta en grados Celsius, ya que la API de Openweathermap
    # nos facilita este dato en grados Kelvin.  
    result = 'Weather forecast for tomorrow in ' + city.capitalize() + ' Temperature: ' + str(round(r['main']['temp'] - 273.15, 2)) + ' ºC'
    print(result)
else:
    print('La ciudad que ha introducido no se encuentra disponible, para más info ejecute el siguiente comando:\n python weather.py -h')