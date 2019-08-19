import config
import requests
from flask import Flask

app = Flask(__name__)

@app.route('/<city>')
def weather(city):
    # api-endpoint 
    api_endpoint = "http://api.openweathermap.org/data/2.5/weather"

    # url para obtener la información sobre una ciudad concreta
    url = api_endpoint + "?q=" + city + "&appid=" + config.api_key
    
    # realizar solicitud GET sobre la url que le pasemos
    r = requests.get(url)

    # devolver resultados en formato JSON
    return r.json()

app.run(host=config.host, port=config.port, debug=config.debug)