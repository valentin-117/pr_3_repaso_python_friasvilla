# Sumar los números pares desde el 2 hasta el 100 (inclusive)
suma = 0

# Usamos range para obtener los números pares desde 2 hasta 100
for numero in range(2, 101, 2):  
    suma += numero

# Imprimimos el resultado
print(f"La suma de los números pares desde 2 hasta 100 es: {suma}")
