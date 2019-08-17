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
$ export FLASK_APP=app.py
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
               siguientes opciones: Madrid, Barcelona, Valencia, Sevilla,
               Palma, Murcia.
```
### Pruebas en local:
Iniciar server:

![run server](https://lh3.googleusercontent.com/_DXMa8qU19SOCVN9WNx5rNyTWDFI53UDKR0481n5RQDCKwDPzEgP64Zf997-N9_rcBitZoEo2dUS)

Ejecución del script `weather.py`:

![run script](https://lh3.googleusercontent.com/Z9XhYi43eqaJrnonTeqp9M2m_XFD48K6Y3ALsE5Ah3kqDusJy-ux4tWFYiLkRhWq9x_iUWCRTy1q)

Seleccionar una ciudad no disponible entre las de prueba y obtener información del script:

![info script](https://lh3.googleusercontent.com/4j6cqyu7475a9-EI3x7OtS6a767Jnp53fUF_67gmyfAQP2WJmFcB2-ztBWU37fGqbJ89UJQMwFGv)

Observar JSON recibido desde la ruta en el navegador:

![json info](https://lh3.googleusercontent.com/VPGaZi9CLicGolbjKGZ5pJUMNr4JAyEPKlTJSJH4VT1D_X4eCLEpX8uXs9qxja1V7lLeJTDLbGHl)