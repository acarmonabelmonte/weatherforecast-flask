from app import index
import os

os.system('FLASK_APP=app.py FLASK_DEBUG=1 python -m flask run')

print("======= Ciudades disponibles =======")
cities = ["Barcelona", "Madrid", "Valencia", "Murcia", "Sevilla", "Galicia"]
for x in cities:
  print('- ' +  x)

print("¿De qué ciudad desea saber el tiempo?")
city = input()

if city.capitalize() in cities:
    index(city)
else:
    print('La ciudad que ha introducido no existe entre las opciones')

