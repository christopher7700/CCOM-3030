#Encabezamiento

##=================================================================                                                 
#   Programador: Chritopher Rodriguez   CCOM 3030    Sección 002     
#   Numero de estudiante: 801-16-7700   Primer Semestre 2020-21       
#   Asignación  #10                      Prof. Rafael J. Colorado       
#   Archivo: asigna10                    Fecha: 20/11/2020
#                                                                   
#=================================================================
#                                                                    
#   Propósito: Este programa calcula las dimensiones de un rectangulo dado el largo y el ancho
#                             
#=================================================================

def main():

    #desplegar proposito
    Desplegar_proposito()

    #ingresar largo y ancho
    Ancho,Largo = Leer_dimensiones()

    #calcular perimetro
    
    Perimetro = Calcular_perimetro(Ancho, Largo)
    
    #calcular area
    Area = Calcular_area (Ancho, Largo)
    
    #desplegar ancho, largo, area y perimetro del rectangulo

    Desplegar_dimensiones (Ancho, Largo, Perimetro, Area)

    
############################################
#Nombre: Desplegar_Proposito
#Proceso: Despliega el proposito del programa
#Recibe (input): Nada
#Develve (output): Nada
#############################################
def Desplegar_proposito():
    print("\n\tEste programa calcula las dimensiones de un rectangulo dado largo y el ancho. ")


############################################
#Nombre: Leer_Dimensiones
#Proceso: Ingresa el ancho y el largo del rectangulo.
#Recibe (input): Nada
#Develve (output): El ancho y el largo del rectangulo.
#############################################
def Leer_dimensiones():

    w = float(input("\tIngrese ancho > 0.0 : "))
    while w <= 0:
        w =float(input("\tIngrese ancho > 0.0 : "))

    l = float(input("\tIngrese largo > 0.0 : "))
    while l <= 0:
        l =float(input("\tIngrese largo > 0.0 : "))

    return w,l


############################################
#Nombre: Calcular_Perimetro
#Proceso: Calcula el perimetro del rectangulo.
#Recibe (input): Ancho y largo del rectangulo.
#Develve (output): Perimetro del rectangulo.
#############################################
def Calcular_perimetro (An, Lar):

    Perimetro=2.0*(An+Lar)

    return Perimetro


############################################
#Nombre: Calcular_Area
#Proceso: Calcula el area del rectangulo
#Recibe (input): Ancho y largo del rectangulo.
#Develve (output): El area del rectangulo
#############################################
def Calcular_area (An,Lar):
    Area=An*Lar
    return Area

##############################################
#Nombre: Desplegar_Dimensiones
#Proceso: Despliega ancho, largo, perimetro y area del rectangulo
#Recibe (input): Ancho, largo, perimetro y area del rectangulo
#Develve (output): Nada
#############################################

def Desplegar_dimensiones (An, Lar, Perimetro, Area):

    print("\n\t<<<Dimensiones del Rectangulo>>>")
    print("\t\tAncho    :",format(An,'3.3f'))
    print("\t\tLargo    :",format(Lar,'3.3f'))
    print("\t\tPerimetro:",format(Perimetro,'3.3f'))
    print("\t\tArea     :",format(Area,'3.3f'))

#################Invocar main############################
continuar = 's'
while continuar == 's' or continuar == 'S' :
    main ()
    continuar = input ("\n\tDesea continuar (s/n): ")
