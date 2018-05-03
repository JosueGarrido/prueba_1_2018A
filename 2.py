
cadena=input("Ingrese cadena")

i=len(cadena)
print(i)

j=0

for i in cadena:
    for j in cadena:
        cadena = cadena.replace(i, j)

    print(cadena)

def escribir():

    archi=open('2.txt','a')
    archi.write(cadena+'\n')
    archi.close()

escribir()