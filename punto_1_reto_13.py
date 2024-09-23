dicc1 = {1: "zoologico", 2: "hipopotamo" , 3: "coctel"}
dicc2 = {"uno" : 54, "dos": 68, "tres":6}

sort_dicc2 = dict(sorted(dicc2.items(), key=lambda valor: valor[1])) # se reordena el diccionario vuelto lista a partir de los valores al definir la funcion key y luego se vuelve diccionario
for llave, valor  in sort_dicc2.items():    # se recorre el diccionario 
    print(f"{valor}", end=" ")  # se imprime los valores

print("\n")

# mismo proceso, en diccionario 1

sort_dicc1 = dict(sorted(dicc1.items(), key=lambda valor: valor[1]))
for llave, valor  in sort_dicc1.items():
    print(f"{valor}", end=" ")