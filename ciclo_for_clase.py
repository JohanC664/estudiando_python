#contador letras
frase = input ("por favor ingrse una frase")
letra = input ("por favor ingrsar la letra a buscar")
contletra = 0

for i in frase:
    if i == letra:
        contletra += 1
print ("la letra '%s' aparece %2i en la frase '%s'. " %(letra,contletra,frase))        