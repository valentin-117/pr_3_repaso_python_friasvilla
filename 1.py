def comprobar_edad(edad):

    return "Eres mayor de edad" if edad > 18 else "NO eres mayor de edad"#funcion que comprueba la edad

#solicita la edad de el usuario
edad = int(input("Introduce tu edad: "))

#se llama a la función y mostramos el resultado
print(comprobar_edad(edad))
