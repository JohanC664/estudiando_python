
estatura = 1
suma = 0
cont = 0
while estatura > 0:
    estatura = float (input("si desea dejar e digitar estaturas digite 0 \n" "por favor ingrese una esatura: " ))
        
    if estatura > 0:
        suma += estatura
        cont += 1
        
if cont > 0:
    print (f"el promedio de las esataturas es {suma/cont}")
        
        
