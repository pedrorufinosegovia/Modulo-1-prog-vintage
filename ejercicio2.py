import screenmalo

valores={"operador1":0, "operador2":0, "clave":0}

tabla = [" ", "+", "-", "x", "/", "%", "//", "^"]

screenmalo.clear()
screenmalo.Print("Op1:", 2, 28)
screenmalo.Print("Op2:", 3, 28)
screenmalo.Print("Sol..:", 2, 1)

def operadores(n):
    if n == "+":
        return 1
    elif n == "-":
        return 2
    elif n == "*":
        return 3
    elif n == "/":
        return 4
    elif n == "%":
        return 5
    elif n == "//":
        return 6
    elif n == "^":
        return 7
    else:
        return 0
    
def numero(cadena):
    try:
        float(cadena)
        return True
    except:
        return False

def pedirnumero():
    valor = screenmalo.Input("introduce un numero o un operador: ", 5, 1)
    while valor != "FIN":
        if numero(valor):
            operador = float(valor)
            
            if valores["clave"] == 0 and valores["operador1"] == 0:
                valores["operador1"] = operador
                screenmalo.Print(valores["operador1"], 2, 33, True)
                valor = screenmalo.Input("introduce un operador o cambia el numero: ",5, 1)
            
            elif valores["clave"] != 0 and valores["operador1"] == 0:
                valores["operador1"] = operador
                screenmalo.Print(valores["operador1"], 2, 33, True)
                valor = screenmalo.Input("introduce un numero : ", 5, 1)
                
            elif valores["clave"] == 0 and valores["operador1"] != 0:
                valores["operador1"] = operador
                screenmalo.Print(valores["operador1"], 2, 33, True)
                valor = screenmalo.Input("introduce un numero o un operador: ",5,1)
            
            elif valores["clave"] != 0 and valores["operador1"] != 0:
                valores["operador2"] = operador
                screenmalo.Print(valores["operador2"], 3, 33, True)
                
                if valores["clave"] == 1:
                    solucion = valores["operador1"] + valores["operador2"]
                
                if valores["clave"] == 2:
                    solucion = valores["operador1"] - valores["operador2"]
                
                if valores["clave"] == 3:
                    solucion = valores["operador1"] * valores["operador2"]
                
                if valores["clave"] == 4:
                    solucion = valores["operador1"] / valores["operador2"]
                
                if valores["clave"] == 5:
                    solucion = valores["operador1"] % valores["operador2"]
                
                if valores["clave"] == 6:
                    solucion = valores["operador1"] // valores["operador2"]
                
                if valores["clave"] == 7:
                    solucion = valores["operador1"] ^ valores["operador2"]
                screenmalo.Print(solucion, 2 , 8)
                
                valores["operador1"] = solucion
                
                screenmalo.Print(valores["operador1"], 2 , 33 , True)
                 
                valores["operador2"] = 0
                
                valores["clave"] = 0
                
                valor = screenmalo.Input("introduce un numero o un operador: ", 5,1, True)
        else:
            valores["clave"] = operadores(valor)
            screenmalo.Print(tabla[valores["clave"]], 4 , 33)
            if valores["clave"] == 0:
                screenmalo.Print("Introduce un dato correcto porfavor ", 8, 1, True)
            valor = screenmalo.Input("introduce un numero o un operador: ", 5, 1)

pedirnumero()
