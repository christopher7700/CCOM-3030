

    



#=================================================================                                                 
#   Programador: Chritopher Rodriguez   CCOM 3030    Sección 002     
#   Numero de estudiante: 801-16-7700   Primer Semestre 2020-21       
#   Asignación  #5                     Prof. Rafael J. Colorado       
#   Archivo: asigna5                    Fecha: 09/18/2020
#    Calcula distancia                                                                 
#=================================================================
#                                                                    
#   Propósito:  dadas las cordenadas calcular la distancia entre los puntos.
#                             
#=================================================================


# Bosquejo de variables
import math 
# Desplegar el proposito
print('\n\tdadas las cordenadas calcular la distancia entre los puntos.')

#Ingresar x1
x1 = float (input("\tIngrese x1: "))

#Ingresar y1
y1 = float (input("\tIngrese y1: "))

#Ingreaar x2
x2 = float (input("\tIngrese x2: "))

#Ingresar y2
y2 = float (input("\tIngrese y2: "))

#calcular la distancia entre las coordenadas
distancia = math.sqrt ( (x2-x1) **2 + (y2-y1) **2)


#Desplegar x1,y1,x2,y2,Distancia

print("\n\t<<<Distancia entre dos puntos>>>\n")
print("\tP1 = (",x1,",",y1,")")
print("\tP2 = (",x2,",",y2,")")
print("\n\tDistancia =",format(distancia,'6.3f'))

input("\n\tOprima ENTER para terminar...")



