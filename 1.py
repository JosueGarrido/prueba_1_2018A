

binario=(input("Ingrese numero binario: "))

i=len(binario)

def calculadora():

    while i>0:
        codigo =binario[i]*(2**i)
        i=i-1
        resultado= resultado+codigo
        print(resultado)
def crear():
    archi=open('1.txt','w')
    archi.close()

def escribir():

    archi=open('1.txt','a')
    archi.write("Josue garrido"+'\n')
    archi.write(binario+'\n')


escribir()