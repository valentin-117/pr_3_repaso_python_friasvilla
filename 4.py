#se crea una lista
notas = [7.5, 3.2, 8.9, 6.4, 5.6, 9.1, 4.7]

# Iniciamos las variables para la nota más baja y la más alta
nota_baja = notas[0]
nota_alta = notas[0]

# Recorremos la lista para encontrar la más baja y la más alta
for nota in notas:
    if nota < nota_baja:
        nota_baja = nota
    if nota > nota_alta:
        nota_alta = nota

# se imprimen los resultados
print(f"La nota más baja es: {nota_baja}")
print(f"La nota más alta es: {nota_alta}")

