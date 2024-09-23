import json
Json = """{
	"jadiazcoronado":{
		"nombres": "Juan Antonio",
		"apellidos": "D��az Coronado",
		"edad":19,
		"colombiano":true,
		"deportes":["F�utbol","Ajedrez","Gimnasia"]
	},
	"dmlunasol":{
		"nombres": "Dorotea Maritza",
		"apellidos": "Luna Sol",
		"edad":25,
		"colombiano":false,
		"deportes":["Baloncesto","Ajedrez","Gimnasia"]
	}
}"""

Deportes = ["F�utbol","Ajedrez","Gimnasia","Baloncesto"]    # se define una lista con los deportes del json
data = json.loads(Json)     # se asigna el json a una variable

def buscar_deporte (dep : int) -> str:  # se define la funcion que toma un deporte como entero para regresar la cadena de los nombres y apellidos que juegan ese deporte
    print("Las personas que practican este deporte son: ")
    for keys, values in data.items():   # se recorre el json
        if Deportes[dep-1] in values.get("deportes"):   # se verifica que el deporte ingresado se encuentre en los deportes del json
               print(f"{values.get("nombres")} {values.get("apellidos")}")  # si resulta encontrarse el deporte, se imprime el nombre y apellido de quien lo juega

def buscar_edad (min_edad : int, max_edad : int) -> str:    # se define la funcion que toma dos valores enteros, para verificar que las edades del json se encuentren dentro del rango de edades 
    existencia = 0
    print("Las personas en este rango de edad son:")
    for keys, values in data.items():   # se recorre las llaves y valores del json vuelto tuplas
        if values.get("edad") > min_edad and values.get("edad") <= max_edad:    # verifica si la edad dentro del json esta dentro del rango de edad
            print(f"{values.get("nombres")} {values.get("apellidos")}") # si se cumple la condicion, imprime el nombre y apellido de quien esta en el rango
            existencia += 1 # si se encuentra alguien en el rango, se asigna un valor diferente a "existencia"
        elif existencia == 0: # si no se encuentran personas en el rango
       		print("No existen personas dentro de este rango de edad")
        


if __name__ == "__main__":
    for i in range(0,len(Deportes)):    # se imprimen los deportes como una lista numerada a partir de 1
        print(f"{i+1}. {Deportes[i]}")
    selec_depor = int(input("Seleccione un deporte de entre los siguientes: ")) # el usuario selecciona un deporte como numero dentro de la lista impresa
    buscar_deporte(selec_depor) # se aplica la funcion sobre el deporte como numero seleccionado
    selec_min_edad = int(input("Ingrese una edad minima para la busqueda: "))   # se ingresa una edad minima para el rango
    selec_max_edad = int(input("Ingrese una edad maxima para la busqueda: "))   # se ingresa una edad maxima para el rango
    buscar_edad(selec_min_edad,selec_max_edad)  # se aplica la funcion sobre las edades ingresadas