def corrector(cadena):
    contador = 0
    corregido = ""
    if 97 <= ord(cadena[0]) <= 122:
        ordmayuscula = ord(cadena[contador]) - 32
        mayuscula = chr(ordmayuscula)
        corregido = corregido + mayuscula
        contador += 1  
    
    while len(cadena)-1 > contador:
        if cadena[contador] in ".,:;" and cadena[contador+1] != " ":
            corregido += cadena[contador]
            corregido = corregido + " "
            contador +=1
            if cadena[contador-1] == "." and  97 <= ord(cadena[contador]) <= 122:
                ordmayuscula = ord(cadena[contador]) - 32
                mayuscula = chr(ordmayuscula)
                corregido = corregido + mayuscula
                contador += 1
            else:
                corregido = corregido + cadena[contador]
                contador += 1
        if cadena[contador] == " " and cadena[contador+1] == " ":
            contador += 1
        else:
            corregido = corregido + cadena[contador]
            contador += 1
    corregido = corregido + cadena[contador]
    return corregido
        
def cuentacaracteres(cadena):
    contador = 0
    while len(cadena) > contador:
        if cadena[contador] == "/" and cadena[contador + 1] == "n":
            caracteres["parrafos"] += 1
            contador += 2
            
        elif cadena[contador] == " ":
            caracteres["palabras"] +=1
            contador += 1
        
        elif cadena[contador] in "aeiouAEIOU":
            caracteres["vocales"] += 1
            if cadena[contador] in "aeiou":
                caracteres["minusculas"] +=1
                contador += 1
            else:
                caracteres["mayusculas"] +=1
                contador += 1
                
        elif cadena[contador] in "qzwsxdcrfvtgbyhnjmklpñQZWSXDCRFVTGBYHNJMKLPÑ":
            caracteres["consonantes"] += 1
            if cadena[contador] in "qzwsxdcrfvtgbyhnjmklpñ":
                caracteres["minusculas"] +=1
                contador += 1
            else:
                caracteres["mayusculas"] +=1
                contador += 1
            
        elif cadena[contador] in "0123456789":
            caracteres["digitos"] +=1
            contador += 1
            
        elif cadena[contador] == ".":
            caracteres["frases"] +=1
            contador += 1
        else:
            caracteres["otroscaracteres"] +=1
            contador += 1
    caracteres["palabras"] += 1
    return caracteres

caracteres = {"palabras": 0, "vocales":0, "consonantes":0,
                "digitos":0,"otroscaracteres":0, "mayusculas":0,
                "minusculas":0, "frases":0, "parrafos":0}

ficheroO = open(input("intoduce un documento de texto:"), "r")
texto = ficheroO.read()
ficheroCorregido = open("correcciones.txt", "a+")

ficheroCaracteres= open("caracteres.txt",  "a+")

done = corrector(texto)
cuentacaracteres(done)
ficheroCorregido.write(done)
ficheroCaracteres.write("palabras:{}, vocales{}, consonates{}, digitos{}, otroscaracteres:{}, mayusculas:{}, minusculas:{}, frases:{}, parrafos:{} /n".format(caracteres["palabras"], caracteres["vocales"], caracteres["consonantes"],
                                                                                                                                                          caracteres["digitos"], caracteres["otroscaracteres"], caracteres["mayusculas"],
                                                                                                                                                          caracteres["minusculas"], caracteres["frases"],caracteres["parrafos"]))
                                                                                                    
ficheroCorregido.close()
ficheroCaracteres.close()
ficheroO.close()

print("se han creado dos nuevos ficheros")
