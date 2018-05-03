from math import pow, pi
def Cubo():
    print("Volumen de un cubo")
    lado= (float)(input("Ingrese el lado: "))

    volumen= pow(lado,3)
    print("El volumen del cubo es: ", '%.2f' %volumen, "m^3")

def PiramideTriangular():

    print("Volumen de una piramide de base triangular")
    base1 = (float)(input("Ingrese lado de la base: "))
    base2 = (float)(input("Ingrese altura de la base: "))
    altura= (float)(input("Ingrese altura de la piramide: "))

    volumen = ((base1*base2)/2)*((1/3)*(altura))
    print("El volumen de la piramide de base triangular es: ", '%.2f' %volumen, "m^3")


def PiramideRectangular():

    print("Volumen de una piramide de base rectangular")
    base = (float)(input("Ingrese lado de la base: "))
    altura = (float)(input("Ingrese altura de la piramide: "))

    volumen = (pow(base,2)*((1/3)*(altura)))
    print("El volumen de la piramide de base rectangular es: ", '%.2f' %volumen, "m^3")


def Esfera():

    print("Volumen de una esfera")
    radio=(float)(input("Ingrese el radio de la esfera: "))
    volumen=(4/3)*pi*pow(radio,3)
    print("El volumen de la esfera es: ", '%.2f'%volumen, "m^3")

opcion=int(input("\nMenu\n--------------------\n\t"
          +"1) Volumen de un cubo\n\t"
          +"2) Volumen de una piramide de base triangular\n\t"
          +"3) Volumen de una piramide de base rectangular\n\t"
          +"4) Volumen de una esfera\n\t"
          +"5) Salir\n\n\t"
          +"Por favor ingrese una opcion: "))

while   (opcion!=5):
    if(opcion == 1):
        Cubo()

    elif(opcion == 2):
        PiramideTriangular()

    elif(opcion == 3):
        PiramideRectangular()

    elif(opcion == 4):
        Esfera()

    elif(opcion == 5):
        break

    else:
        print("\nFavor ingrese opciones validas\n")

    opcion = int(input("\nMenu\n--------------------\n\t"
                       + "1) Volumen de un cubo\n\t"
                       + "2) Volumen de una piramide de base triangular\n\t"
                       + "3) Volumen de una piramide de base rectangular\n\t"
                       + "4) Volumen de una esfera\n\t"
                       + "5) Salir\n\n\t"
                       + "Por favor ingrese una opcion: "))