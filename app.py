import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index(city):
    # city = 'Barcelona'
    api_endpoint = "http://api.openweathermap.org/data/2.5/weather"
    apikey = "953886b865382df790a3cda9564a301e"
    url = api_endpoint + "?q=" + city + "&appid=" + apikey
    
    r = requests.get(url.format(city)).json()
    
    weather = {
        'city' : city,
        'temperature' : round(r['main']['temp'] - 273.15, 2)
    }
    
    result = 'Weather forecast for tomorrow in ' + city.capitalize() + ' Temperature: ' + str(weather['temperature']) + ' ºC'
    
    print (result)
    return result

if __name__ == '__main__':
    app.run(debug=True)