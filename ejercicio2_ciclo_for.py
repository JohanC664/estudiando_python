n = int (input("ingresa # de empleados"))
cont = 0
cont1= 0
gasto = 0
for ini in range (n):
    sueldo = float (input("ingresar el valor sueldo del {ini} empleado"))
    gasto = gasto + sueldo
if sueldo >= 1300000 and sueldo <= 3000000:
    cont += 1
elif sueldo > 3000000:
    cont1 += 1
print ("los gastos de la empresa total ", gasto)
print ("empleados que ganan entre 1.300.000 y 3.000.000 son:", cont)
print ("empleados que ganan mas de 3000.000 son:", cont1)
    
    