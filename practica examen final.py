"""

Desplegar proposito
Leer la lista de puntuaciones
calcular la media aritmetica de la lista de puntuaciones
Calcular la cantidad de puntuaciones iguales o mayores a la media
Desplegar resultados

"""

def main():
    
    #Desplegar proposito
    Desplegar_Proposito()
    
    #Leer la lista de puntuaciones
    puntuaciones = Leer_Puntuaciones()
    
    #calcular la media aritmetica de la lista de puntuaciones
    media = Calcular_Media(puntuaciones)
    
    
    #Calcular la cantidad de puntuaciones iguales o mayores a la media
    sobreMedia = Calcular_Sobre(puntuaciones,media)
    
    
    #Desplegar resultados
    Desplegar_Resultados (puntuaciones,media,sobreMedia)

######################################
#nombre:
#Proceso:
#Input:nada
#output:nada
######################################
def Desplegar_Proposito():
    print(""""\tEste programa...""")


    
######################################
#nombre:
#Proceso:
#Input:nada
#output:lista de puntuaciones
######################################
def Leer_Puntuaciones():
    
    #Leer cantidad de puntuaciones
    cantidad = int(input("\tIngrese cantidad de putuaciones: "))
    while cantidad <=0:
        cantidad = int(input("\tIngrese cantidad de putuaciones: "))

    #Iniciar la lista  a Nula o vacia
    puntuaciones = []

    #Ingresar las puntuaciones y agregarlas a lalista
    for k in range(1,cantidad+1):

        #Leer la proxima puntuacion
        print("\tIngrese la puntuacion",k,")",end="")
        dato = int(input())
        while dato <0 or dato >100:
            print("\tIngrese la puntuacion",k,")",end="")
            dato = int(input())
            
        #Agregar el dato a la lista
        puntuaciones.append(dato)

    #devolver lista de puntuaciones
    return puntuaciones 
    

######################################
#nombre:Calcular_Media
#Proceso:
#Input:Lista de puntuaciones
#output:media aritmetica
######################################         
def Calcular_Media(puntuaciones):
    return sum (puntuaciones)/len(puntuaciones)


#####################################
#nombre:Calcular_Sobre
#Proceso:
#Input:(puntuaciones,media)
#output:puntuaciones iguales o mayor q la media
######################################
def Calcular_Sobre(points,mean):

    #contador a 0
    counter=0

    #Cotejar en la lista
    for element in points:
        if element>= mean:
            counter += 1

    #Devolver el contador
    return counter


#####################################
#nombre:Desplegar_Resultados 
#Proceso:
#Input: (puntuaciones,media,sobreMedia)
#output:Resultados
######################################
def Desplegar_Resultados (points,mean,overMean):
    print("\n\t<<< Resultados>>>")

    #desplegar puntuaciones
    print("\n\tLas puntuaciones son:\n")
    for suscrito in range(len(points)):
        print("\t",suscrito+1,")",points[suscrito],sep=" ")
    print("\n\tLa media es:",format(mean,'6.2f'))
    print("\tSobre la media:",overMean)
    
        
####################################################################
continuar = 's'
while continuar == 's' or continuar == 'S':
    main()
    continuar = input ("\n\tDesea continuar? (s/n): ")
print("\nGracias por usar el programa..")
                       
