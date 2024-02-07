sum_grupo1 = 0
sum_grupo2 = 0
sum_grupo3=0
for m in range (6):
    mañana = int(input("por favor ingrse las 6 edades de la mañana"))
    sum_grupo1 = sum_grupo1 + mañana
    
for t in range (7):
    tarde= int(input("por favor ingrese las 7 edades de la tarde"))
    sum_grupo2 = sum_grupo2 + tarde

for n in range (12):
    noche = int(input("por favor ingrese las 12 edades de la noche"))
    sum_grupo3=sum_grupo3+noche


promedio1=sum_grupo1/6
promedio2=sum_grupo2/7
promedio3=sum_grupo3/12

if promedio1> promedio2 and promedio1> promedio3:
    print ("promedio grupo mañana tiene un promedio de edades mayores")
elif promedio2 > promedio1 and promedio2 > promedio3:
    print ("el grupo tarde tiene un promedio de edades mayores")
else:
    print ("el grupo noche tiene un promedio de edades mayores")

print (f"la suma de las edades de la mañana es: {sum_grupo1} y el promedio es {promedio1}")
print (f"la suma de las edades de la tarde es: {sum_grupo2} y el promedio es {promedio2}")
print (f"la suma de las edades de la tarde es: {sum_grupo3} y el promedio es {promedio3}")