def mezcla_dicc ( dicc1, dicc2):    # se define la funcion mezcla de diccionario
    for keys in dicc2:  # se recorren las llaves del segundo diccionario
        if keys in dicc1:   # se buscan las llaves dentro del primer diccionario
            dicc2[keys] = dicc1[keys]   # si se encuentra, se igualan los valores
    dicc1.update(dicc2) # se actualizan y agregan los valores del segundo diccionario al primero
    return dicc1    # se retorna el diccionario actualizado
if __name__ == "__main__":
    dicc1 = {1: "zoologico", 2: "hipopotamo" , 3: "coctel"}
    dicc2 = {"uno" : 54, 2 : 68, "tres":6}
    dicc3 = mezcla_dicc(dicc1,dicc2)
    print(dicc3)