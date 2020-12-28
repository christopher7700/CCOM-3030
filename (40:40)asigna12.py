
##=================================================================                                                 
#   Programador: Chritopher Rodriguez   CCOM 3030    Sección 002     
#   Numero de estudiante: 801-16-7700   Primer Semestre 2020-21       
#   Asignación  #12                     Prof. Rafael J. Colorado       
#   Archivo: asigna12                   Fecha: 11/12/2020
#    Quiz                                                               
#=================================================================
#                                                                    
#   Propósito:tEste programa, dadas las respuestas de un quiz, las transforma en una
#       lista, las corrige y las compararlas con la CLAVE. Luego, despliega
#       los resultados del mismo"""
#                             
#=================================================================




Clave =['A','B','D','C','D'] #Constante Global

def main () :

    
    #Desplegar Proposito
    Desplegar_proposito()
    
    # Leer el nombre y numero de est
    Nombre, Numero = Leer_ID()
    
    #leer las respuestas y pasarlas a una lista.
    Respuesta = Leer_respuesta()
    
    
    #Corregir la lista de respuesta.
    Correctas,Resultado = Corregir_prueba(Respuesta)

    
    #Desplegar los resultados.   
    Desplegar_resultados (Nombre,Numero,Respuesta,Correctas,Resultado)

############################################
#Nombre:Desplegar_proposito
#Proceso:
#Input:nada
#Output:nada
#############################################
    
def Desplegar_proposito():

    print("""\n\tEste programa, dadas las respuestas de un quiz, las transforma en una
        \tlista, las corrige y las compararlas con la CLAVE. Luego, despliega
        \tlos resultados del mismo""")

############################################
#Nombre:Leer_ID
#Proceso:Ingresa name y number
#Input:nada
#Output:nombre y numero de estudiante
#############################################

def Leer_ID():
    name = input("\n\tIngrese su nombre: ")
    number = input("\n\tIngrese su numero: ")

    return name,number

############################################
#Nombre:Leer_respuesta
#Proceso: Ingresa las respuestas a una lista 
#Input:nada
#Output:Lista de las respuestas
#############################################

def Leer_respuesta():

    #Iniciar la lista de respuestas a nula o vcia

    respuestas = []

    #Leer las respuestas

    for k in range(len(Clave)):
        
        #Ingresar respuesta
        
        print("\tIngrese la respuesta", k+1,")",end='')
        answer = input().upper()

        #Input Validation
        
        while answer not in ['A','B','C','D','E']:
            print("\n\tERROR. Debe ser una letra de la A-E")
            print("\tIngrese la respuesta: ", k+1,")",end='')
            answer = input().upper()
        
        #Pasar la respuesta a la lista
                   
        respuestas.append(answer)
                   
    #Devolver lista de respuestas
                   
    return respuestas


############################################
#Nombre: Corregir_prueba
#Proceso: Corrige lista de respuestas y desplega con la clave
#Input:respuestas
#Output:nada
#############################################
def Corregir_prueba(respuestas):

    #Iniciar lista de datos a nula
    resultado = []


    # Iniciar el Contador de respuestas correctas
    right= 0
    
    #Corregir la prueba

    for indice in range (len(Clave)):

        #Comparar cade elemento de Clave con el elemento correspondiente
         #en respuestas.

        if Clave [indice] == respuestas[indice]:
            right += 1
            resultado.append("correcta")
        else:
            resultado.append("Incorrecta")

    return right, resultado

############################################
#Nombre: Desplegar_resultados
#Proceso: Despliega el nombre, número de estudiante, la lista de respuestas del
#         estudiante,cantidad de respuestas correctas y la lista de resultados.
#Input: Nombre, Numero, lista con Clave, Lista de respuestas, cantidad de corrrectas
#       y lista de resultados. 
#Output:nada
#############################################
def Desplegar_resultados (Nombre,Numero,Respuesta,Correctas,Resultado):
    print ("\n\t<<<Resultados de la Prueba>>>\n")
    print ("\tNombre del estudiante: ", Nombre)
    print ("\tNúmero de estudiante: ", Numero)

    print ("\n\tClave\t\tRespuestas\tResultados")

    for suscrito in range (len(Clave)):
        print ("\t", suscrito+1, ") ", Clave[suscrito], "\t\t", Respuesta [suscrito],
         "\t\t ", Resultado[suscrito])

    print ("\n\tCantidad de correctas: ", Correctas)

    if Correctas >= 3:
            print ("\n\t", Nombre, "APROBADO.")
    else:
            print ("\n\t", Nombre, "REPROBADO.")
    
###############MAIN##########################
Desplegar_proposito()

continuar = 's'
while continuar =='s' or continuar=='S':
    main()
    continuar = input ("\n\t¿Desea continuar? (s/n): ")


