def menu_principal():
    while True:
        print("Menú Principal:")
        print("pulse 2. Juego de Dados")
        print("pulse 3. nombre de Alumnos")
        print("pulse 4. Valor de Voletas")
        print("pulse 5. Contraseña")
        print("pulse 6. Calculadora de Factura con IVA")
        print("pulse 7. menu de metodos")
        print("pulse 8. precio y venta frutas")
        print("pulse 9. cesta de compra")
        print("pulse 10. nota alumnos")
        print("pulse 11. Salir")
        

        opcion = input("Ingrese el número del ajercicio al que desea ir: ")

        if opcion == "2":
            juego_de_dados()
        elif opcion == "3":
            nombre_de_alumnos()
        elif opcion == "4":
            valor_de_voleta()
        elif opcion == "5":
            validar_contraseña()
        elif opcion == "6":
            calcular_factura_con_iva()
        elif opcion == "7":
            menu_2()
        elif opcion == "10":
            eje10()
        elif opcion == "8":
            eje8_frutas()
        elif opcion == "9":
            eje9_cesta()
        elif opcion == "11":
            print("¡Hasta luego!")
            break
        else:
            print("Opción que no esta válida. Por favor, ingrese un número del 1 al 11.")
            



#numero 2 juego de dados

def juego_de_dados():
    import random

    jugador1 = random.randint(1, 6)
    jugador2 = random.randint(1, 6)

    print("Álvaro tiró un dado y obtuvo:", jugador1)
    print("Bárbara tiró un dado y obtuvo:", jugador2)

    if jugador1 > jugador2:
        print("¡Álvaro gana!")
    elif jugador1 < jugador2:
        print("¡Bárbara gana!")
    else:
        print("¡Empate!")




#ejercicio 3 - alumnos
def nombre_de_alumnos():
    nombre = input("Ingrese su nombre: ")
    sexo = input("Ingrese su sexo (M/F): ")

    if (sexo == "M" and nombre > "N") or (sexo == "F" and nombre < "M"):
        print("Usted pertenece al Grupo A.")
    else:
        print("Usted pertenece al Grupo B.")

def calculadora_de_entradas():
    edad = int(input("registre su edad: "))

    if edad < 4:
        print("Entrada gratis.")
    elif 4 <= edad <= 18:
        print("Precio de la entrada es: $30000.")
    else:
        print("Precio de la entrada es: $50000.")




#ejercicio 4 valor voleta
def valor_de_voleta():
    edad=int("por favor ingrese su edad para calcular el valor que debe pagar")
    if edad < 4:
        print("puede ingresar de manera gratuita")
    elif edad > 4 and edad <18:
        print("debe pagar 30000")
    elif edad > 18 and edad < 100:
            print ("debe pagar 50000")
    else:
            print ("edad invalida, lo sentimos")



#ejercicio 5 contraseña
def validar_contraseña():
    contraseña_correcta = "contraseña"
    intentos = 3

    while (True):
        contraseña_ingresada = input("Ingrese la contraseña: ")

        if contraseña_ingresada == contraseña_correcta:
            print("Contraseña correcta. Acceso permitido.")
            break
        else:
            print(f"Contraseña incorrecta intentalo de nuevo")




# ejercicio 6 factura con iva
def calcular_factura_con_iva(cantidad_sin_iva=None, porcentaje_iva=21):
    if cantidad_sin_iva is None:
        cantidad_sin_iva = float(input("Ingrese la cantidad sin IVA: "))

    total_factura = cantidad_sin_iva * (1 + porcentaje_iva / 100)
    print(f"Total de la factura con {porcentaje_iva}% de IVA: ${total_factura:.2f}")




#ejercicio 7 menu dos de metodos
def menu_2 ():
    lista_menu2 = []
    while True:
        print("\n")
        print("1. Añadir número a la lista")
        print("2. Añadir número de la lista en una posición")
        print("3. Longitud de la lista")
        print("4. Eliminar el último número")
        print("5. Eliminar un número")
        print("6. Contar números")
        print("7. Posiciones de un número")
        print("8. Mostrar números")
        print("9. Salir")
        opcion = int(input("Dime opción:"))
        if opcion == 1:
            num = int(input("Dime un número:"))
            lista_menu2.append(num)
        elif opcion == 2:
            num = int(input("Dime un número:"))
            pos = int(input("Dime una posición (empezando por 1):"))
            if pos > len(lista_menu2):
                print("Posición incorrecta")
            else:
                lista_menu2.insert(pos - 1,num)
        elif opcion == 3:
            print("Longitud de la lista: %d", len(lista_menu2))
        elif opcion == 4:
            if len(lista_menu2)>0:
                print("El último elemento es %d y lo borramos.", lista_menu2.pop())
            else:
                print("La lista está vacía")
        elif opcion == 5:
            pos = int(input("Dime una posición (empezando por 1):"))
            if pos > len(lista_menu2):
                print("Posición incorrecta")
            else:
                print("El elemento es %d y lo borramos.", lista_menu2.pop(pos - 1))
        elif opcion == 6:
            num = int(input("Dime un número:"))
            print("El número %d aparece %d veces en la lista." % (num,lista_menu2.count(num)))
        elif opcion == 7:
            num = int(input("Dime un número:"))
            indice_buscar = 0
            print("Posiciones: ",end="")
            for indice in range(0,lista_menu2.count(num)):
                indice_buscar = lista_menu2.index(num,indice_buscar)
                indice_buscar +=1
                print(indice_buscar," ",end="")
            print()
        elif opcion == 8:
            for num in lista_menu2:
                print(num," ",end="")
            print()
        elif opcion == 9:
            break
        else:
            print("Opción incorrecta")




#ejercicio 8 precios frutas
def eje8_frutas():
    precios = {"manzana": 2, "naranja": 1500, "pera": 1200, "piña": 3000, "durazno": 1600}
    while True:
        fruta = input("Dime el nombre de la fruta vendida:")
        if fruta.lower() not in precios:
            print("Fruta no existe.")
        else:
            cantidad = int(input("Dime la cantidad de frutas que has sido vendidas:"))
            print("El precio es de %f" % (cantidad * precios[fruta]))
        opcion = input("¿Quieres vender otra fruta (s/n)")
        while opcion.lower() != "s" and opcion.lower() != "n":
            opcion = input("¿Quieres vender otra fruta (s/n)")
        if opcion.lower() == "n":
            break




#eje 9 cesta de compra
def eje9_cesta():
    cesta = {}
    continuar = True
    while continuar:
        item = input('Introduce un artículo: ')
        precio = float(input('Introduce el precio de ' + item + ': '))
        cesta[item] = precio
        continuar = input('¿Quieres añadir mas artículos a la lista (Si/No)? ') == "Si"
    coste = 0
    print('Lista de la compra')
    for item, precio in cesta.items():
        print(item, '\t', precio)
        coste += precio
    print('Coste total: ', coste)



def eje10 ():
    alumnos = {}
    registro = {}
    cantida_digitar=int(input("digite la cantidad de alumnos que se almacenaran"))
    for a in range (cantida_digitar):
        alumno=input("por favor digite el nombre del alumno: ")
    
        while alumno in alumnos:
            print ("el alumno ya esta registrado")
            alumno= input("por favor digite el nombre del alumno: ")
        notas = []
        nota = int(input(f"ingresa la nota de {alumno}: (digite numero negativo para finalizar)"))
        while nota > 0:
            notas.append(nota)
            nota = int(input(f"ingresa la nota de {alumno}: (digite numero negativo para terminar"))
            diccionario = {
        alumno:  notas
        }
        print(diccionario)
        
menu_principal()