n_alturas = int(input("ingrese la cantidad de alturas que desea digitar"))
suma = 0
promedio = 0
cont = 0

while cont < n_alturas:
    altura = float (input("ingrese la altura"))
    suma = suma + altura
    cont = cont + suma
    promedio = suma / n_alturas
print (f"el promedio de las alturas es:{promedio}")
