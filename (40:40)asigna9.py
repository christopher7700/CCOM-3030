
##=================================================================                                                 
#   Programador: Chritopher Rodriguez   CCOM 3030    Sección 002     
#   Numero de estudiante: 801-16-7700   Primer Semestre 2020-21       
#   Asignación  #9                      Prof. Rafael J. Colorado       
#   Archivo: asigna9                    Fecha: 20/11/2020
#    Dimension de cilindro                                                               
#=================================================================
#                                                                    
#   Propósito: Este programa calcula las dimensiones del cilindro
#                             
#=================================================================
import math

def main ():
        
    #Desplegar el propósito del programa
    Desplegar_proposito ()


    #Ingresar el radio y la altura del cilindro
    Radio,Altura = Leer_dimensiones()

    #Calcular el área de la superficie del cilindro 
    Area = Calcular_area(Radio,Altura)

    #Calcular el volumen del cilindro
    Volumen = Calcular_volumen(Radio,Altura)
    
    #Desplegar el radio, el volumen, el área y el volumen del cilindro
    Desplegar_dimensiones(Radio,Altura,Volumen,Area)


 ##############################################
# Nombre: Desplegar_proposito
# Proceso:  Desplega Proposito      
# Input:  nada
# Output: nada
##############################################   
def Desplegar_proposito ():
    print("""\n\tEste programa dados el radio y la altura de un cilindro circular recto, calcule
     \ty despliegue el área de la superficie y el volumen del cilindro.""")

 ##############################################
# Nombre: Leer_dimensiones
# Proceso:  Ingresa radio y altura     
# Input:  nada
# Output: radio y altura
##############################################     
def Leer_dimensiones():
    Radio = float(input("\n\tingrese el radio: "))
    while Radio <= 0.0:
        Radio = float(input("\n\tingrese el radio: "))
        
    Altura = float(input("\tingrese la altura: "))
    while Altura <= 0.0:
        Altura = float(input("\tingrese la altura: "))
    return Radio, Altura

 ##############################################
# Nombre: Calcular_dimensiones
# Proceso:  Calcula area   
# Input:  radio y altura
# Output: area 
##############################################

def Calcular_area (Radio,Altura):
    Area = 2 * 3.14 * Radio ** 2 + 2 * math.pi * Radio * Altura
    return Area

 ##############################################
# Nombre: Calcular_volumen
# Proceso:  Calcula volumen   
# Input:  radio y altura
# Output: volumen
##############################################  


def Calcular_volumen(Radio,Altura):
    Volumen = math.pi * Radio ** 2 * Altura
    return Volumen

 ##############################################
# Nombre: Despliega_dimensiones
# Proceso:Desplegar dimensiones  
# Input:  radio, la altura, el área de la superficie y el volumen 
# Output: nada
##############################################  
def Desplegar_dimensiones (Radio,Altura,Volumen,Area):
   print ("\n\t<<<Dimensiones del cilindro>>>\n")
   print ("\tAltura ========>", format (Altura, '.2f'))
   print ("\tRadio =========>",format (Radio, '.2f'))
   print ("\tÁrea ==========>", format (Area,'.2f'))
   print ("\tVolumen =======>", format(Volumen, '.2f'))
   
###########################
continuar = 's'
while continuar == 's' or continuar == 'S' :
    main ()
    continuar = input ("\n\tDesea continuar (s/n): ")
