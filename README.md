# Weather Forecast with Python and Flask
Servidor de pronóstico del tiempo y un cliente de línea de comandos creados con Python y su framework Flask.
El servidor se conecta a la siguiente api externa para obtener la información climatológica.
Weather API from OpenWeather: [https://openweathermap.org/api](https://openweathermap.org/api)

### Prerrequisitos

 - Instalar Python en su máquina:
   [https://www.python.org/downloads/](https://www.python.org/downloads/)
   
 - Posteriormente instalar las siguientes librerías o paquetes a través de la consola:
```
$ pip install Flask
$ pip install requests
$ pip install argparse
```
### Instalación y ejecución
Descargue una copia de la aplicación desde GitHub y realice los siguientes pasos:

Ejecute el siguiente comando desde la carpeta raíz del proyecto para iniciar el servidor:
```
$ export FLASK_APP=hello.py
$ flask run
 * Running on http://127.0.0.1:5000/
```

A continuación ejecute desde la consola de comandos el script `weather.py` pasándole por parámetro la ciudad sobre la que obtener la predicción climatológica:

Ejemplo:
```
$ python weather.py --city=Madrid
```
Resultado:
```
Weather forecast for tomorrow in Madrid Temperature: 36.0 ºC
```

Se han limitado las ciudades para realizar las pruebas, para obtener información al respecto ejecute el comando `python weather.py -h` y obtendrá dicha información:
```
$ python weather.py -h
usage: weather.py [-h] [--city CITY]

optional arguments:
  -h, --help   show this help message and exit
  --city CITY  Ciudad a obtener el tiempo. Por favor, seleccione entre las
               siguientes opciones:Madrid, Barcelona, Valencia, Sevilla,
               Palma, Murcia.
```
