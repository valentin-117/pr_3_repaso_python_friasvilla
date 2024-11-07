#generamos la tabla de multiplicar
numero = 554  

# Usamos un rango de 1 a 10 para multiplicar
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
