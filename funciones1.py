def inicio():
    
    print ("menu principal")
    print ("seleccione la opcion correcta:")
    print ("1. operacion sumar")
    print ("2. operacion resta")
    print ("3. operacion multiplicar")
    print ("4. operacion dividir")
    
def main():
    while True:
        inicio()
        opcion = int(input("seleccione la opcion"))
        if opcion == 1:
            print ("ha seleccionado la suma")
            num1= int(input("ingrese el numero 1: "))
            num2= int(input("ingrese el numero 2: "))
            sumar= num1 + num2
            print (f"el resultado de la suma es: {sumar}")
        elif opcion == 2:
            print ("has seleccionado operacion resta")
            num1= int(input("ingrese el numero 1: "))
            num2= int(input("ingrese el numero 2: "))
            restar = num1 - num2
            print (f"el resultado de la resta es: {restar}")
        elif opcion==3:
            print ("has seleccionado la operacion multiplicar")
            num1= int(input("ingrese el numero 1: "))
            num2= int(input("ingrese el numero 2: "))
            multiplicar = num1 * num2
            print (f"el resulatdo de la multiplicacion es {multiplicar}")
        elif opcion == 4:
            print ("has escogido la opcion divisio")
            num1= int(input("ingrese el numero 1: "))
            num2= int(input("ingrese el numero 2: "))
            division= num1 / num2
            print (f"el resultado de la division es: {division}")
        elif opcion == 5:
            print ("hasta luego")
        
        else:
            print ("por favor escoja una opcion valida")
            
        print ("opcion no valida, seleccione una opcion valida")
        
main()
        