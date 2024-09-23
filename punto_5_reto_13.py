import json
import requests
from pprint import pprint

def Imprimir_Json(Json):    # se define la funcion para tomar un json proporcionado y analizar si el valor encontrado es otro diccionario para poder definir su metodo de impresion
    for k,v in Json.items():
        if isinstance(v, list): #verificar si esta como elemento lista
            if isinstance(v[0], dict): # verificar si es un diccionario
                print(f"Llave: {k}, Valor(Otro diccionario): \n")
                for i,j in v[0].items():
                    print(f"Llave: {i} , Valor: {j}")
        else:
            print(f"Llave: {k} , Valor: {v}")
url = ['https://api.agify.io?name=santiago','https://dog.ceo/api/breeds/image/random','https://catfact.ninja/fact']
for i in range(len(url)):
    Api=requests.get(url[i]) # se hace una solicitud de dato a la api
    if Api.status_code == 200: # se verifica que la solicitud haya sido aprobada por el servidor
        Api=Api.json()  # la solicitud de dato se convierte a un json legible para el programa
        Imprimir_Json(Api)  # se imprime el json
        print("\n")
    else:
        print('Error en la solicitud, detalles:', Api.text)