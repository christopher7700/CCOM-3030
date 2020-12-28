

##=================================================================                                                 
#   Programador: Chritopher Rodriguez   CCOM 3030    Sección 002     
#   Numero de estudiante: 801-16-7700   Primer Semestre 2020-21       
#   Asignación  #11                     Prof. Rafael J. Colorado       
#   Archivo: asigna11                   Fecha: 11/12/2020
#    Estadisticas                                                               
#=================================================================
#                                                                    
#   Propósito: Este programa calcular la media y
#   desv est. de un conjunto de datos
#   usando listas y funciones
#                             
#=================================================================
import math

########################################################
# Nombre: Main()
# Proceso:Invocar las demas funciones
# Input: Nada
# Output:nada
########################################################

def main ():
    #Desplegar el Proposito

    Desplegar_proposito()
    
    #Leer la lista de datos
    
    Listadedatos = Leer_datos()

    #Calcula la media aritmetica de la lista de datos

    Media = Calcular_media(Listadedatos)
    
    #Calcular Desviacion

    Desviacion= Calcular_desviacion(Listadedatos,Media)
    
    # Calcular Desviacion
    
    Desplegar_estadisticas(Listadedatos,Media,Desviacion)

   
########################################################
# Nombre: Desplegar_proposito()
# Proceso:Desplegar el Proposito
# Input: Nada
# Output:nada
########################################################

def Desplegar_proposito():
    print(""""\n\tEste programa calcular la media y
    \tdesv est. de un conjunto de datos
    \tusando listas y funciones""")

########################################################
# Nombre: Leer_datos()
# Proceso:Lee datos
# Input: nada
# Output: lista de datos
########################################################

def Leer_datos():

    #ingresr la cantidad de datos.

    n = int(input("\n\tIngrese cantidad de datos > 1:"))
    while n <= 1:
        n = int(input("\n\tIngrese cantidad de datos > 1:"))

    #Inciciar la lista a Nula o Vacia.

    x = []

    # Ingresar y agregar datos.

    for i in range (1,n+1):
        
        #Leer un dato.
        
        print("\tIngrese el dato", i , "): ", end="")
        dato = float (input())
        while dato <= 0.0:
            print("\tERROR: El dato debe ser mayor que cero (0).")
            print("\tIngrese el dato", i , "): ", end="")
            dato = float(input())
 
        #pasar el dato ingresado a la lista.
        
        x.append (dato)
              
    return x

########################################################
# Nombre: Calcular_media(Losdatos)
# Proceso:Calcula la media aritmetica
# Input: lista de datos
# Output: la media de la lista de los datos
########################################################
def Calcular_media (Losdatos):

        
    media = sum (Losdatos) / len (Losdatos)

    return media 


########################################################
# Nombre: Calcular_desviacion
# Proceso: calcula desviacion estandard de la lista de datos
# Input: lista de datos,la media  
# Output: desviacion de la lista de datos
########################################################
def Calcular_desviacion(Listadedatos,Media):
    desviMedia = 0.0
    
    for x in Listadedatos :
        desviMedia += (x - Media) **2
        
    return math.sqrt (desviMedia/(len(Listadedatos)-1))

########################################################
# Nombre: Desplegar_estadisticas
# Proceso: Desplegar las estadisticas 
# Input: lista de datos,la media y la desviacion 
# Output: Nada
########################################################

def Desplegar_estadisticas(x, Promedio, Desvi):

    print("n\tLista de Datos")
    for indice in range(len(x)):
        print("\t\t",indice +1,")",format(x[indice],"6.2f"),sep = '')


    print("\n\tEstadisticas:")
    print("\n\tDato mayor= ", format(max(x) , '6.2f'))
    print("\tDato menor= ", format(min(x) , '6.2f'))
    print("\tMedia====== ", format(Promedio, '6.2f'))
    print("\tDesviacion= ", format(Desvi ,'6.2f'))

######INVOCAR MAIN######################################
continuar = 's'
while continuar =='s' or continuar =='S':
    main ()
    continuar = input ("\n\tDesea continuar? (s/n): ")
    

