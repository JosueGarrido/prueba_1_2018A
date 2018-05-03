
codigo = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
letra = ['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
lista=[codigo,letra]

mensaje=input("Ingrese mensaje a codificar")


def crear():
    archi=open('3.txt','w')
    archi.close()

def grabar():

    archi=open('3.txt','a')
    archi.write(mensaje)

grabar()