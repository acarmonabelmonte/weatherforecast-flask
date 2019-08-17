import requests
from flask import Flask

app = Flask(__name__)

@app.route('/weather-forecast/<city>')
def getWeatherInfo(city):
    # api-endpoint 
    api_endpoint = "http://api.openweathermap.org/data/2.5/weather"

    # apikey de prueba para conectar con la API de Openweathermap
    apikey = "953886b865382df790a3cda9564a301e"

    # url para obtener la información sobre una ciudad concreta
    url = api_endpoint + "?q=" + city + "&appid=" + apikey
    
    # realizar solicitud GET sobre la url que le pasemos
    r = requests.get(url)

    # devolver resultados en formato JSON
    return r.json()

if __name__ == '__main__':
    app.run(debug=True)