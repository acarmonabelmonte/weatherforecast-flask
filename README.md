# Weather Forecast with Python and Flask
Servidor de pronóstico del tiempo y un cliente de línea de comandos creados con Python y su framework Flask.
El servidor se conecta a la siguiente api externa para obtener la información climatológica.
Weather API from OpenWeather: [https://openweathermap.org/api](https://openweathermap.org/api)

### Prerrequisitos
 
 - Consola Bash de Linux (disponible al instalar git en tu máquina):
   [https://git-scm.com/downloads/](https://git-scm.com/downloads/)
   
 - Python:
   [https://www.python.org/downloads/](https://www.python.org/downloads/)
   
 - Posteriormente instalar las siguientes librerías o paquetes a través de la consola:
```
$ pip install Flask
$ pip install requests
$ pip install argparse
```
### Instalación y ejecución
Descargue una copia de la aplicación desde GitHub y realice los siguientes pasos:

Ejecute los siguientes comandos desde la carpeta raíz del proyecto para iniciar el servidor:
```
$ export FLASK_APP=server.py
$ python server.py
 * Running on http://127.0.0.1:5000/
```

A continuación, con el server activo, ejecute desde la consola de comandos el script `weather.py` pasándole por parámetro la ciudad sobre la que obtener la predicción climatológica:

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
               siguientes opciones: Madrid, Barcelona, Valencia, Sevilla,
               Murcia.
```
### Pruebas en local:
Iniciar server:

![run server](https://lh3.googleusercontent.com/DID45l-euCcPJt5Xi3mNnwvZIv0JXQLzQqIBqVIwn7dCHfigFaxdy-eWhEes5JuNZ2uS0a3bj1OH)

Ejecución del script `weather.py`, seleccionar una ciudad no disponible entre las de prueba y obtener información del script:

![run script](https://lh3.googleusercontent.com/yfkp4ASD2wqDnigmWe9xZ82nGYjT-UWMHpCOjb7vX8N1dZuWWHRKnzZ7_mXVX4p17NJq9fEecO7m)

Observar JSON recibido desde la ruta en el navegador:

![json info](https://lh3.googleusercontent.com/l9Fu2JT3A4VY1BH2BdY5e_dCIjkdDTFDtIE82in4sstAxx2DxwRLqmiANzPUC20Ri3wriWOq2nQf)
