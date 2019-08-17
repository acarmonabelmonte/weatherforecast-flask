import requests

# array con ciudades de España de ejemplo
print('========== Ciudades disponibles ==========')
cities = ["Barcelona", "Madrid", "Valencia", "Murcia", "Sevilla", "Galicia"]
for x in cities:
      print('- ' +  x)

# seleccionar la ciudad
print("¿De qué ciudad desea saber el tiempo?")
city = input()

# realizamos la petición GET si la ciudad se encuentra entre las opciones de ejemplo
if city.capitalize() in cities:
    # api-endpoint 
    api_endpoint = "http://127.0.0.1:5000/weather-forecast/"

    # url
    url = api_endpoint + city

    # realizar solicitud GET sobre la url pasada
    r = (requests.get(url)).json()

    weather = {
        'city' : city,
        'temperature' : round(r['main']['temp'] - 273.15, 2)
    }

    result = 'Weather forecast for tomorrow in ' + city.capitalize() + ' Temperature: ' + str(weather['temperature']) + ' ºC'

    print(result)
else:
    print('La ciudad que ha introducido no existe entre las opciones')