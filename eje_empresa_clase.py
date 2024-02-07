cont = 0
numero1= 0
acum = 0
acum1=0
empleado = int (input("cuantos empleados quiere verificar"))
while cont < empleado :
    sueldo = int(input("ingrese su sueldo"))
    numero1=numero1+sueldo
    cont += 1
    print ("el empelado numero", cont , "resive un sueldo de", sueldo)
    if sueldo >= 1300000 and sueldo <= 3000000:
        acum += 1
    elif sueldo >= 3000000:
        acum1 += 1
print ("la capacidad de empleados que cobran entre $ 10.000.000 y $300.000 es: ", acum)
print ("la capacidad de empleados que cobran entre $ 3.000.000 o mas es: ", acum1)
print ("el importe que gasta la empresa en personal es: ", numero1)